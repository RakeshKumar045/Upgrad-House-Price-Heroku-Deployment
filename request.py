import requests

url = 'http://localhost:5000/house_pred'

json_body_value_for_model = {"sqft": 1500, "place": 2, "yearsOld": 5, "totalFloor": 10, "bhk": 3}

res = requests.post(url, json=json_body_value_for_model)

print("Model Predicted Result : ", res.json())
