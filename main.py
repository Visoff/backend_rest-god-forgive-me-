# API
# REST API
# RealTime API

# CRUD - Create, Read, Update, Delete

import flask

app = flask.Flask(__name__)

storage = {"data":"hello world"}

@app.get("/")
def index():
    f = open("index.html", "r")
    return f.read()

# GET / - hello world
@app.get('/<root_path>')# endpoint
def root(root_path):
    if root_path in storage:
        return storage[root_path]
    return ""

@app.post('/<root_path>')
def root_post(root_path):
    data = flask.request.data
    storage[root_path] = data+"!"
    return 'OK'

@app.delete('/<root_path>')
def root_delete(root_path):
    storage[root_path] = ""
    return 'OK'

app.run(host='0.0.0.0', port=8080)
