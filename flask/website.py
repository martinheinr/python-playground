from flask import Flask

""" app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, World!' """


app = Flask("hello")

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'