import requests

URL = "http://127.0.0.1:5000/"
obj = {'files': ['file1', 'file2']}

responses = requests.post(URL, json = obj)
print(responses.text)