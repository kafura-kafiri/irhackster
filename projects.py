from flask import Blueprint, render_template, jsonify, request, redirect
from bson import ObjectId
from config import projects

blu = Blueprint('projects', __name__, url_prefix='/projects')


@blu.route('/<_id>')
def get(_id):
    project = projects.find_one({'_id': ObjectId(_id)})
    return render_template('basicals/get.html', project=project)


@blu.route('/+', methods=['GET'])
def get_new():
    return render_template('basicals/new.html')


@blu.route('/+', methods=['POST'])
def post_new():
    project = { # date and author
        'cover_image': request.form['base_article[cover_image_id]'],
        'name': request.form['base_article[name]'],
        'one_liner': request.form['base_article[one_liner]']
    }
    result = projects.insert_one(project)
    _id = str(result.inserted_id)
    return redirect('/projects/' + _id + '/$')


@blu.route('/<_id>/$', methods=['GET'])
def get_edit(_id):
    project = projects.find_one({'_id': ObjectId(_id)})
    return render_template('basicals/edit.html')


@blu.route('/<_id>/$', methods=['POST'])
def post_edit(_id):
    pass


@blu.route('/<_id>/*', methods=['POST'])
def delete(_id):
    projects.delete_one({'_id': ObjectId(_id)})


