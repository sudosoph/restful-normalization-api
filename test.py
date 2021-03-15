import requests

URL = "http://127.0.0.1:5000/"
obj = {'name': 'file'}

response = requests.post(URL, data = obj)
print(response.text)