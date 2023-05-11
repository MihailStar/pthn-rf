# Задача B

from os.path import dirname, join

import pandas as pd

input_b = input()
grouping_column, statistics_column, name_of_statistics = input_b.split(" ")

titanic_df = pd.read_csv(join(dirname(__file__), "./titanic.csv"))
series_group = titanic_df.groupby(grouping_column)[statistics_column]

if name_of_statistics == "min":
    series = series_group.min()
elif name_of_statistics == "max":
    series = series_group.max()
else:
    series = series_group.count()

for index, value in series.to_dict().items():
    print(index, value)
