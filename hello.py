from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p> Hello, World !<p>"

@app.route("/hello")
def hello():
    name = request.args.get("name","Flask")
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User{escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post{post_id}'

@app. route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath{escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project Page'

@app.route ('/about')
def about():
    return 'The about page'