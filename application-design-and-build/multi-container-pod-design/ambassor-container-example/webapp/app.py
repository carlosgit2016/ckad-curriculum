from crypt import methods
from flask import Flask
import os
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_car():
    body = request.get_json()
    print(body)
    # new_car(body)

def get_database():
    user = os.environ.get('MONGO_DB_USERNAME')
    password = os.environ.get('MONGO_DB_PASSWORD')
    MONGO_URL = os.environ.get('MONGO_URL')

    CONNECTION_STRING = f'mongodb://{user}:{password}@{MONGO_URL}/'
    client = MongoClient(CONNECTION_STRING)

    return client

def new_car(*docs):
    db = get_database()['rl_cars']
    collection_name = db['cars']

    collection_name.insert_many(docs)

if __name__ == "__main__":
    dbname = db_create()
    app.run(port=os.environ.get('PORT'), debug=False, host='0.0.0.0')