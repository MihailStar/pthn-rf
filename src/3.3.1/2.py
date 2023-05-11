# Задание 2

import requests

URL = "https://pokeapi.co/api/v2"

id = 35
response = requests.get(f"{URL}/pokemon/{id}").json()
name = response["name"]
abilities = ", ".join([ability["ability"]["name"] for ability in response["abilities"]])

print(name, abilities, sep=", ", end="")
