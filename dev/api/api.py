from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import dumps

import canary

app = Flask("canary")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('spotify', default='')
parser.add_argument('deezer', default='')
parser.add_argument('google-play', default='')
parser.add_argument('itunes', default='')

class Canary(Resource):
    def get(self):

        args = parser.parse_args()
        spotify = args['spotify']
        deezer = args['deezer']
        googleplay = args['google-play']
        itunes = args['itunes']

        return canary.suggest(
            spotify_username=spotify,
            deezer_username=deezer,
            googleplay_username=googleplay,
            itunes_username=itunes)

api.add_resource(Canary, '/')

if __name__ == '__main__':
     app.run(port='4242')
