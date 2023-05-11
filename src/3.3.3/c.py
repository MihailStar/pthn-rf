# Задача C

from os.path import dirname, join

import pandas as pd

input_c = input()
min_age, pclass, parch = map(int, input_c.split())

titanic_df = pd.read_csv(join(dirname(__file__), "./titanic.csv"))
filtered_df = titanic_df[
    (titanic_df["Age"] > min_age)
    & (titanic_df["Pclass"] == pclass)
    & (titanic_df["Parch"] == parch)
]
series = filtered_df.groupby("Survived")["PassengerId"].count()

number_of_non_survivors = series[0] if 0 in series else 0
number_of_survivors = series[1] if 1 in series else 0
number_of_all = number_of_non_survivors + number_of_survivors

if number_of_all == 0:
    print(0)
else:
    proportion = number_of_survivors / number_of_all
    truncated_proportion = int(proportion)

    print(
        truncated_proportion
        if truncated_proportion == proportion
        else round(proportion, 4)
    )
