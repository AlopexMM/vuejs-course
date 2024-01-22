import json
with open('evolution.json', 'r') as json_file:
    json_data = json.loads(json_file.read())

    for obj in json_data:
        print(obj)
        break
