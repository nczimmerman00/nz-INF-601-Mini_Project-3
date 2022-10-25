# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
