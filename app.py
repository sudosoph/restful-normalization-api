#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def post():   
    if request.method == 'POST':
        data = request.get_data()
        files = data.decode().replace('files=','').split('&')
        # data = request.form['files']
        # files = data.getlist()
    # check if array is empty or not
    if files:    
        # iterate a received array
        # return data
        for file in files:
        #   print every single filename
            return file
    else: 
         # if empty, return {'status': 'ok'}
        return {'status': 'ok'}
    
if __name__ == '__main__':
    api.run(debug=True, port=5000)