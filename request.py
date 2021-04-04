import requests

url = 'http://localhost:5000/house_pred'
res = requests.post(url, json={'experience': 2, 'test_score': 9, 'interview_score': 6})

print("Model Predicted Result : ", res.json())
