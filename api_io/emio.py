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
    def get(self, longitude, latitude, longitude2, latitude2):
        # Send to javi's module
        # tweets = <javiModule>.getTweets(<params>)
        # Send to Jake's module
        # emioData = <Jake's module>.getEmotion(tweets)
        # for i in emioData:
        #   put into json like below
        j = {
        "longitude":longitude,
        "latitude":latitude,
        "Emotion":"Happy!"}
        return j
class Emotion_Filter_Topic(Resource):
    def get(self, longitude, latitude, longitude2, latitude2, keyword):
        # Prep for filter keyword
        j = 0
        return j

class Emotion_Filter_Emotion(Resource):
    def get(self, longitude, latitude, longitude2, latitude2, emotion)
        # prep for emotional filter
        j = 0;
        return j

#Connect classes to routes.
api.add_resource(Emotion_Meta, '/emio/intro')
api.add_resource(Emotion_location, '/emio/<int:longitude>,<int:latitude>,<int:longitude2>,<int:latitude2>')
api.add_resource(Emotion_Filter_Topic, '/emio/<int:longitude>,<int:latitude>,<int:longitude2>,<int:latitude2>/<string:keyword>')
api.add_resource(Emotion_Filter_Emotion, '/emio/<int:longitude>,<int:latitude>,<int:longitude2>,<int:latitude2>/<string:emotion>')

if __name__ == '__main__':
    emio.run()
