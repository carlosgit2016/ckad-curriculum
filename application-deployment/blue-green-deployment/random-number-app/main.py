from crypt import methods
from numpy import random
from os import environ
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_random_number():
    return str(random_number())

@app.route('/version', methods=['GET'])
def get_version():
    return environ.get('VERSION')

def random_number():
    return round(random.random(1)[0] * 100)

if __name__ == "__main__":
    app.run(port=environ.get('PORT'), debug=False, host='0.0.0.0')