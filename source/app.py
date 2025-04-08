from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'OK'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/error')
def error():
    raise Exception('This is an error!')