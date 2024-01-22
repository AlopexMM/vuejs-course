import requests

res = requests.get('http://localhost:8000/dollar_api?source=Blue&date=2023-12-19')

if res.status_code == 200:
    print(res.json())
else:
    print(res.status_code)