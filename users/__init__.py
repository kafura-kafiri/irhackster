from flask import Blueprint, render_template, request
from config import users
from utility import obj2str, request_json
from flask_login import login_required, current_user

blu = Blueprint('users', __name__, url_prefix='/users')

messages = {
    'saved',
    'required',
    'segment',
    'invalid',
    'already',
    'character',
    '2num',
    'bad',

    'updated',
    'removed',
    'not_saved',
    'not_removed',
    'saved',
}


@blu.route('/me')
#@login_required
def get_profile():
    return render_template('users/profile.html')


@blu.route('/me$', methods=['GET', 'POST'])
#@login_required
def update_profile():
    from pymongo import ReturnDocument
    try:
        node = request.values['node']
        _json = request_json(request, specific_type=None)
        user = users.find_one_and_update(
            {'_id': current_user._id},
            {"$set": {node: _json}},
            return_document=ReturnDocument.AFTER
        )
        id = user.id
        current_user.__dict__ = user
        current_user.id = id
    except: pass
    return render_template('users/profile_plus.html')