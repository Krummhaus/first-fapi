import requests

r = requests.post("http://localhost:8000/h2i", json={"who": "Mom"})
print(r.json())