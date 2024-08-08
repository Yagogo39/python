import requests

url = "http://pokeapi.co/api/v2/pokemon?limit=1000"

response = requests.get(url)
list = response.json()["results"]

for pokemon in list:
    print(pokemon["name"])