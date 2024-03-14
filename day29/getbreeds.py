import requests

r = requests.get('https://dog.ceo/api/breeds/list/all')
json_response = r.json()

for breed, sub in list(json_response['message'].items()):
    print(f"{breed}: {sub if len(sub) > 0 else ''}")
