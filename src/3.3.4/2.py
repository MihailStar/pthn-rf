# Задание 2

from typing import Any, Dict

from pymongo import MongoClient

client: MongoClient[Dict[str, Any]] = MongoClient()


db = client["sample_weatherdata"]
collection = db["data"]
count = collection.count_documents({"pressure.value": {"$lt": 1000}})

print(count)


db = client["sample_restaurants"]
collection = db["restaurants"]
count = collection.count_documents(
    {"$and": [{"borough": "Bronx"}, {"name": {"$regex": ".*Food.*"}}]}
)

print(count)


db = client["sample_supplies"]
collection = db["sales"]
min = collection.find_one(sort=[("customer.age", 1)])
max = collection.find_one(sort=[("customer.age", -1)])

if min == None or max == None:
    raise Exception()

min_age = min["customer"]["age"]
max_age = max["customer"]["age"]

print(min_age, max_age, sep=",")
