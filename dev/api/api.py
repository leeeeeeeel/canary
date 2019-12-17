""" Api responsable for handling applications requests for music suggestion """

from flask import Flask, request, abort
from flask_restful import Resource, Api
import voluptuous as v

import canary

app = Flask("canary")
api = Api(app)

class Canary(Resource):
    def post(self):
        history = request.json.get('history')

        try:
            schema = v.Schema(v.All([{
                v.Required('music_id'): v.All(str, v.Length(min=5, max=15)),
                v.Required('relevance'): v.All(float, v.Range(min=0, max=1))
                }], v.Length(min=1)))

            schema(history)
        except v.MultipleInvalid as e:
            # history data doesn't match requisitions
            abort(400)

        return canary.suggest(history), 200

api.add_resource(Canary, '/')

if __name__ == '__main__':
     app.run(port='4242')
