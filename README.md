RESTful API for Audio Normalization
=============

This simple application allows you to pass in an audio file via URL, which will be audio normalized using the Pydub library method, and returned in the same directory.

Setup
-----

- Install Python 3 and git.
- Clone or download the repository.
- Run `setup.sh` (Linux, OS X, Cygwin) or `setup.bat` (Windows).
- Run `FLASK_ENV=development flask run` to start the server (Linux, OS X, Cygwin) or `set FLASK_ENV=development flask run` (Windows).
- In a separate terminal window, run `python3 test.py` to test the POST request.

<img src="https://github.com/sudosoph/simple-normalization-api/blob/main/img/output.png" width="600">



