from flask import Flask, render_template, url_for

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

@app.route('/image')
def image_example():
    img_url = url_for('static', filename='flaskLogo.png')
    return render_template('image.html', url =img_url, title='Flaks Image', img_url=img_url)