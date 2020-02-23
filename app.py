from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello %s' % username

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)