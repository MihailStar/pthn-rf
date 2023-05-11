# Задача D

from os.path import dirname, join

import pandas as pd

input_d = input()
fill_value = float(input_d)

titanic_df = pd.read_csv(join(dirname(__file__), "./titanic.csv"))
age_series: "pd.Series[float]" = titanic_df["Age"].fillna(fill_value)
age_average = age_series.mean()

print(round(age_average, 4))
