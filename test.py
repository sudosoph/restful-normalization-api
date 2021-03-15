import requests

URL = "http://127.0.0.1:5000/"
obj = {'files': ['file1', 'file']}

responses = requests.post(URL, data = obj)
print(responses.text)