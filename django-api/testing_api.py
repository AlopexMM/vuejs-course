import requests

res = requests.get('http://localhost:8000/dollar_api')

print(res.json())