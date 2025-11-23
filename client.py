"""
client for testing the prediction endpoint

usage example:
$ python3 client.py

"""
import json
import requests

# dataset for several predictions
data = [
    [5.1, 3.5, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 4.2, 1.5],
    [6.0, 2.2, 4.0, 1.0],
    [5.5, 2.3, 4.0, 1.3],
    [6.3, 3.3, 6.0, 2.5],
]

url = "http://0.0.0.0:8000/predict/"
predictions = []
for record in data:
    data = {"features": record}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json)
    predictions.append(response.json()["predicted_class"])
print("Predictions:", predictions)
