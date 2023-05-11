# Задача A

from typing import Any, Dict

from pymongo import MongoClient


def get_ages_sum() -> int:
    url = "mongodb://127.0.0.1:27017"
    client: MongoClient[Dict[str, Any]] = MongoClient(url)
    db = client["db"]
    users = db["users"]

    total_age = 0

    for user in users.find():
        total_age += user["age"]

    return total_age
