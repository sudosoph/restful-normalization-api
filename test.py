import requests

URL = "http://127.0.0.1:5000/"
obj = {
    "files": [
        "test-audios/M5_b49_w5_orig.wav",
        "test-audios/M5_b49_w6_orig.wav",
        "test-audios/M5_b50_w1_orig.wav",
        "test-audios/M5_b50_w2_orig.wav",
        "test-audios/M5_b50_w3_orig.wav",
        "test-audios/M5_b50_w4_orig.wav",
    ]
}

responses = requests.post(URL, json=obj)
print(responses.text)
