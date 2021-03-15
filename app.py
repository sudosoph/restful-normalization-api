#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def post():   
    if request.method == 'POST':
        data = request.args.getlist('files')
    # check if array is empty or not
    if data:    
       # iterate a received array
        for arg in data:
            # print every single filename
            return "{}\n".format(arg)
    else: 
         # if empty, return {'status': 'ok'}
        return {'status': 'ok'}
    
if __name__ == '__main__':
    api.run(debug=True, port=5000)