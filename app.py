#!flask/bin/python

"""RESTful server for audio normalization implemented using the Pydub library"""

from flask import Flask, request
from flask_restful import Api, Resource
from pydub import AudioSegment, effects
import os

UPLOAD_DIRECTORY = "/test-audios/output"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["POST"])
def post():
    files = request.get_json(force=True)
    #print(files)
    result = []
    # check if array is empty or not
    if files:
        # iterate a received array
        for files, file in files.items():
            # print every single filename
            for i, file in enumerate(file):
                with open(os.path.join(UPLOAD_DIRECTORY, file), "wb") as fp:
                    fp.write(file)
                #result.append(file)
            #for x in result:
                #print(x)
                # rawsound = AudioSegment.from_file("{}".format(x))
                # normalizedsound = effects.normalize(rawsound)
                # normalizedsound.export("output" + "{}".format(x))
            #return "Normalized Files: " + " ".join(result)
    # if empty
    return {"status": "ok"}


if __name__ == "__main__":
    api.run(debug=True, port=5000)
