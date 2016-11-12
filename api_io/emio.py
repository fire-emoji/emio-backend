#import flask items
from flask import Flask, request
from flask_restful import Resource, Api
#import sqlalchemy for connecting to database
from sqlalchemy import create_engine
# json for dumpin'
import json

# connect flask and api to our app
emio = Flask(__name__)
api = Api(emio)

# Class for each api route
class Emotion_Meta(Resource):
    def get(self):
        return "Hello world!"

class Emotion_location(Resource):
    def get(self, longitude, latitude):
        j = {'longitude':longitude, 'latitude':latitude, 'Emotion':"Happy!"}
        return j

#Connect classes to routes.
api.add_resource(Emotion_location, '/emio/<int:longitude>,<int:latitude>')
api.add_resource(Emotion_Meta, '/emio/intro')

if __name__ == '__main__':
    emio.run()
