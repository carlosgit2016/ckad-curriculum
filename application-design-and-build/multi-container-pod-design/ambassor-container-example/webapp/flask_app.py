from flask import Flask
from flask_app import app as application

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

def db_create():
    pass

if __name__ == "__main__":
    db_create()
    app.run(port=80, debug=False)