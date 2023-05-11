# Задача A

from typing import Tuple

input_a = input()


def make_plural(num: int, titles: Tuple[str, str, str]) -> str:
    abs_num = abs(num)
    rem_10 = abs_num % 10
    rem_100 = abs_num % 100

    if rem_10 == 1 and rem_100 != 11:
        index = 0
    elif rem_10 >= 2 and rem_10 <= 4 and (rem_100 < 10 or rem_100 >= 20):
        index = 1
    else:
        index = 2

    return titles[index]


print(make_plural(int(input_a), ("комментарий", "комментария", "комментариев")))
