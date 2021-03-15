#!flask/bin/python

"""RESTful server for audio normalization implemented using the
Flask-RESTful extension."""

from flask import Flask, jsonify
from flask_restful import Api, Resource, marshal
from pydub import AudioSegment

app = Flask(__name__)
api = Api(app)

files = [
    {
        'id': 1,
        'path': u'audio1.wav'
    },
    {
        'id': 2,
        'path': u'audio2.wav'
    }
]

file_fields = {
    'path': fields.String,
    'uri': fields.Url('file')
}

class FileListAPI(Resource):
    def post(self):
        file = {
            'id': files[-1]['id'] + 1 if len(files) > 0 else 1,
            'path': args['path'],
            'uri': args['uri']
        }
        files.append(file)
        return {'task': marshal(file, file_fields)}, 201

api.add_resource(FileListAPI, '/files', endpoint='files')

if __name__ == '__main__':
    app.run(debug=True)