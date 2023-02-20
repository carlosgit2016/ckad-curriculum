from crypt import methods
from numpy import random
from os import environ
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_random_number():
    payload = {
        'randomnumber': str(random_number()),
        'version': environ.get('VERSION'),
        'pod_name': environ.get('POD_NAME'),
        'pod_uid': environ.get('POD_UID'),
        'pod_ip': environ.get('POD_IP')
    }

    return payload


def random_number():
    return round(random.random(1)[0] * 100)


if __name__ == "__main__":
    app.run(port=environ.get('PORT'), debug=False, host='0.0.0.0')
