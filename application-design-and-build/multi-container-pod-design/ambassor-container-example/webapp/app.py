from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

def db_create():
    pass

if __name__ == "__main__":
    db_create()
    app.run(port=os.environ.get('PORT'), debug=False, host='0.0.0.0')