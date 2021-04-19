#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource
from pydub import AudioSegment, effects
import logging


app = Flask(__name__)
api = Api(app)

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

@app.route("/", methods=["POST"])
def post():
    files = request.get_json(force=True)
    for i in files["files"]:
        rawsound = AudioSegment.from_wav("test-audios/" + i)
        #normalizedsound = effects.normalize(rawsound)
        l = logging.getLogger("pydub.converter")
        l.setLevel(logging.DEBUG)
        l.addHandler(logging.StreamHandler())
        normalized_sound = match_target_amplitude(rawsound, -5.0)
        normalized_sound.export("test-audios/output/" + i)
    return {"status": "ok"}


if __name__ == "__main__":
    api.run(debug=True, port=5000)
