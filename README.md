RESTful API for Audio Normalization
=============

This simple application allows you to pass in an audio file via URL, which will be audio normalized using the Pydub library method, and returned in the same directory.

Setup
-----

- Install Python 3 and git.
- Run `setup.sh` (Linux, OS X, Cygwin) or `setup.bat` (Windows)
- Run `./rest-server.py` to start the server (on Windows use `flask\Scripts\python rest-server.py` instead)
- Open `http://localhost:5000/` on your web browser to run the client
