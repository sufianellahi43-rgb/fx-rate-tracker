import requests

rate = 1.17
threshold = 1.15

if rate > threshold:
    message = {"currency": "EUR", "rate": rate}
    response = requests.post("http://localhost:5000/webhook", json=message)
    print(response.text)