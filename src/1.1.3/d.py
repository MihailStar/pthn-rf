# Задача D

from collections import defaultdict
from typing import DefaultDict, List, Tuple

input_d = input()


def count_letters(text: str) -> List[Tuple[str, int]]:
    letter_to_number_of_letters: DefaultDict[str, int] = defaultdict(lambda: 0)

    for char in text:
        if char.isalpha():
            letter_to_number_of_letters[char.lower()] += 1

    return sorted(letter_to_number_of_letters.items())


def format_for_print(pair: Tuple[str, int]) -> str:
    letter, counter = pair

    return f"{letter} {counter}"


print("\n".join(map(format_for_print, count_letters(input_d))))
