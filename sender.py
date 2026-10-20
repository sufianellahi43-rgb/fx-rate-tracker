import requests

message = {"currency": "EUR", "rate": 1.17}

response = requests.post("http://localhost:5000/webhook", json=message)

print(response.text)