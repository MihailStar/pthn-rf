# Задача D

from collections import Counter

input_d = input()


def is_real(string: str) -> bool:
    values = Counter(Counter(string).values()).values()
    lenght = len(values)

    return lenght == 1 or (lenght == 2 and any(value == 1 for value in values))


print(is_real(input_d))
