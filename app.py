#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource
from pydub import AudioSegment, effects


app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["POST"])
def post():
    files = request.get_json(force=True)
    for i in files["files"]:
        rawsound = AudioSegment.from_wav("test-audios/" + i)
        normalizedsound = effects.normalize(rawsound)
        normalizedsound.export("test-audios/output/" + i)
    return {"status": "ok"}


if __name__ == "__main__":
    api.run(debug=True, port=5000)
