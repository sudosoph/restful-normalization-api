#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# files = [{'name': 'file1'}, {'name', 'file2'}, {'name', 'file3'}]

@app.route('/', methods=['POST'])
def post():
        return request.form['files']

if __name__ == '__main__':
    api.run(debug=True, port=5000)