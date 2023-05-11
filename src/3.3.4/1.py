# Задание 1

import json
import sqlite3
from os.path import dirname, join
from typing import Dict, List, Literal, Tuple, TypeAlias, TypedDict

connection = sqlite3.connect(join(dirname(__file__), "./db.sqlite"))
cursor = connection.cursor()


# query = "SELECT name FROM sqlite_master WHERE type='table';"
# results = cursor.execute(query).fetchall()

# print(results)


# query = "SELECT sql FROM sqlite_master WHERE name='films'"
# results = cursor.execute(query).fetchall()

# print(results)


query = "SELECT movie, year, rating_ball FROM films WHERE director = ' Эльдар Рязанов' AND year > 1970;"
results: List[Tuple[str, int, float]] = cursor.execute(query).fetchall()


class Movie(TypedDict):
    year: int
    rating_ball: str


Movies: TypeAlias = Dict[Literal["Эльдар Рязанов"], List[Dict[str, Movie]]]
movies: Movies = {"Эльдар Рязанов": []}

for movie, year, rating_ball in results:
    trimmed_movie = movie.rstrip()

    movies["Эльдар Рязанов"].append(
        {trimmed_movie: Movie(year=year, rating_ball=str(rating_ball))}
    )

with open(join(dirname(__file__), "./1.json"), "w", encoding="utf-8") as fl:
    json.dump(movies, fl, ensure_ascii=False, indent="  ")
    fl.write("\n")

connection.close()
