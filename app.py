#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, jsonify, abort
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class AudioFiles(Resource):
    def post(self):
        return jsonify({'files': [file1, file2]})

    #def post(self):
        # create json request app 
        # { files: [file1, file2, ...] }
        # strings

        # print what you receive in body
        # python script that does a post request

        # Return 201 CREATED
        #return "", 201

api.add_resource(AudioFiles, "/<string:name>")

if __name__ == '__main__':
    api.run(debug=True, port=5000)