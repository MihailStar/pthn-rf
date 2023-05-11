# Задача E

from typing import Dict

input_e = input()
char_to_number_of_chars: Dict[str, int] = dict()

for char in input_e:
    if char in char_to_number_of_chars:
        char_to_number_of_chars[char] += 1
    else:
        char_to_number_of_chars[char] = 1

char, _number_of_chars = max(char_to_number_of_chars.items(), key=lambda item: item[1])

print(char)
