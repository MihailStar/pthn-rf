# Задача B

from typing import Callable, Tuple

input_b = input()

CHAR_TO_CODE = {
    "0": ord("0"),
    "9": ord("9"),
    "A": ord("A"),
    "Z": ord("Z"),
    "a": ord("a"),
    "z": ord("z"),
    "А": ord("А"),
    "Я": ord("Я"),
    "а": ord("а"),
    "я": ord("я"),
}

is_digit: Callable[[str], bool] = lambda char: (
    CHAR_TO_CODE["0"] <= ord(char) <= CHAR_TO_CODE["9"]
)

is_latin_letter: Callable[[str], bool] = lambda char: (
    (CHAR_TO_CODE["A"] <= ord(char) <= CHAR_TO_CODE["Z"])
    or (CHAR_TO_CODE["a"] <= ord(char) <= CHAR_TO_CODE["z"])
)

is_cyrillic_letter: Callable[[str], bool] = lambda char: (
    (CHAR_TO_CODE["А"] <= ord(char) <= CHAR_TO_CODE["Я"])
    or (CHAR_TO_CODE["а"] <= ord(char) <= CHAR_TO_CODE["я"])
)


def count_symbols(text: str) -> Tuple[int, int, int]:
    counter = {"digits": 0, "letters": 0, "other": 0}

    for char in text:
        if is_digit(char):
            counter["digits"] += 1
        elif is_latin_letter(char) or is_cyrillic_letter(char):
            counter["letters"] += 1
        else:
            counter["other"] += 1

    return (counter["letters"], counter["digits"], counter["other"])


print("\n".join(map(str, count_symbols(input_b))))
