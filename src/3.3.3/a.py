# Задача A

from os.path import dirname, join

import pandas as pd

input_a = input()
min_age = int(input_a)

titanic_df = pd.read_csv(join(dirname(__file__), "./titanic.csv"))
number_of_rows, _number_of_columns = titanic_df[titanic_df["Age"] > min_age].shape

print(number_of_rows)
