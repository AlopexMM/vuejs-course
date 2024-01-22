import requests

res = requests.get('http://localhost:8000/dollar_api?date=2023-12-19')

if res.status_code == 200:
    print(res.json())
else:
    print(res.status_code)

res = requests.get('http://localhost:8000/dollar_api?date=2023-12-20')

if res.status_code == 200:
    print(res.json())
else:
    print(res.status_code)