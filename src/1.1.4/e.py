# Задача E

input_e = input()

ARABIC_NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMAN_NUMBERS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def convert_roman_number_to_arabic_number(roman_number: str) -> str:
    previous_index: int | None = None
    result = 0

    for char in roman_number:
        index = ROMAN_NUMBERS.index(char)

        if previous_index and ARABIC_NUMBERS[previous_index] < ARABIC_NUMBERS[index]:
            result += ARABIC_NUMBERS[index] - ARABIC_NUMBERS[previous_index] * 2
        else:
            result += ARABIC_NUMBERS[index]

        previous_index = index

    return str(result)


print(convert_roman_number_to_arabic_number(input_e))
