#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource
from pydub import AudioSegment, effects
import os

FILES_DIRECTORY = os.getcwd() + "/test-audios"

if not os.path.exists(FILES_DIRECTORY):
    os.makedirs(FILES_DIRECTORY)

app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["POST"])
def post():
    files = request.get_json(force=True)
    for key, val in files.items():
        for i in val:
            with open(os.path.join(FILES_DIRECTORY, i), "rb") as fp:
                rawsound = AudioSegment.from_file(fp)
                normalizedsound = effects.normalize(rawsound)
                normalizedsound.export("output" + i)
                fp.close()
    return {"status": "ok"}


if __name__ == "__main__":
    api.run(debug=True, port=5000)
