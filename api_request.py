import requests

req = requests.get("https://swapi.dev/api/people/6/")
person = req.json()
print(f"name is -> {person['name']}")
print(f"Birth date is -> {person['birth_year']}")