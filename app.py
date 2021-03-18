#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['POST'])
def post():   
    files = request.get_json(force=True)
    print(files)
    #files = data.decode().replace('files=','').split('&')
        # data = request.form['files']
        # files = data.getlist()
    # check if array is empty or not
    if files:    
        # iterate a received array
        # return data
        for files, file in files.items():
        #   print every single filename
            #return '{}\n'.format()
            #result = [i for i in file]
            return '\n'.join('{}'.format(i) for i in file)
    # if empty, return {'status': 'ok'}
    return {'status': 'ok'}
    
if __name__ == '__main__':
    api.run(debug=True, port=5000)