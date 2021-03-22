import requests

URL = "http://127.0.0.1:5000/"
obj = {"files": ["test1.wav", "test2.wav"]}

responses = requests.post(URL, json=obj)
print(responses.text)
