#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

import os
from flask import Flask, jsonify, abort, send_file, send_from_directory
from pydub import AudioSegment

UPLOAD_DIRECTORY = "/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

api = Flask(__name__)

"""Upload File"""
@api.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename),
    "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201

if __name__ == '__main__':
    api.run(debug=True, port=5000)