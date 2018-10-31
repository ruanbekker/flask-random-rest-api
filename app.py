import os, json, random
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson import json_util

env_mongo_uri = os.getenv('MONGODB_URI')

app = Flask(__name__)
app.config['MONGO_URI'] = env_mongo_uri
mongo = PyMongo(app)

names = ['ruan', 'stefan']

@app.route('/')
def main():
    data = mongo.db.people.find_one({"name": random.choice(names)})
    return json.dumps(data, default=json_util.default)

if __name__ == '__main__':
    app.run()
