from flask import Flask, jsonify
from projects import blu

app = Flask(__name__)
app.register_blueprint(blu)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users/api_token')
def dummy():
    return jsonify({
        "client_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJoYWNrc3RlciIsImlhdCI6IjIwMTgtMDUtMDRUMDk6NTg6MDMrMDAwMCIsImV4cCI6IjIwMTgtMDUtMDRUMTE6NTg6MDMrMDAwMCIsInJuZCI6ImU3YmZiOTA3MjdhMTFhOTM3MmM2N2QyY2Q3NzEyMGFkIn0.zy3KhjI1vA0_sRDzLf9uMEWkB3uP-W3jyU8pT09ZoVyb8M2xI6lTUPc-p_SbTxvNgViL0zOWyYTa31ZGZOl5pw",
        "user_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJoYWNrc3RlciIsImlhdCI6IjIwMTgtMDUtMDRUMDk6NTg6MDMrMDAwMCIsImV4cCI6IjIwMTgtMDUtMDRUMTE6NTg6MDMrMDAwMCIsInJuZCI6IjMxMDI5ODk1ZWEwNDU0MGI4NmI0YWVlMzVjZGY3M2ZhIiwidXNlciI6eyJpZCI6NDg3MzAyLCJlbWFpbCI6ImthZnVyYS5rYWZpcmlAZ21haWwuY29tIn19.raz39eX30cnxWhUB9Q3OLRdAlPyiJEkMPJ00CjW8q_1mAbl1D_CLk-FRxYZ8-oUANF2FV_6aKIxp-u_xXyhmqQ"
    })


@app.route('/v2/projects/<_id>', methods=['POST', 'GET', 'OPTION', 'PATCH'])
def dummy_2(_id):
    return ''


if __name__ == '__main__':
    app.run(debug=True)
