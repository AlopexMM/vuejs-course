import requests

res = requests.get('http://localhost:8000/dollar_api?source=Oficial')

print(res.json())

res = requests.get('http://localhost:8000/dollar_api?source=Blue')

print(res.json())