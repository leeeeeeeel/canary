from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask("canary")
api = Api(app)

class Canary(Resource):
    def get(self):
        return "100 top rated songs"

class Spotify(Resource):
    def get(self, username):
        return "given spotify username return 100 song suggestion"

class GooglePlay(Resource):
    def get(self, username):
        return "given google play username return 100 song suggestion"


api.add_resource(Canary, '/')
api.add_resource(Spotify, '/spotify/<username>') # Route_1
api.add_resource(GooglePlay, '/google-play/<username>') # Route_2

if __name__ == '__main__':
     app.run(port='4242')
