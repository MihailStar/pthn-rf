# Задание 1

import requests

URL = "https://the-one-api.dev/v2"
TOKEN = ""

id = requests.get(f"{URL}/book").json()["docs"][1]["_id"]
number_of_chapters = requests.get(f"{URL}/book/{id}/chapter?limit=1").json()["total"]
number_of_characters = requests.get(
    f"{URL}/character?limit=1",
    headers={"Authorization": f"Bearer {TOKEN}"},
).json()["total"]

print(number_of_chapters, number_of_characters, sep=",", end="")
