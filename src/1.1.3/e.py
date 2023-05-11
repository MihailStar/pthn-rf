# Задача E

from collections import OrderedDict
from sys import version_info
from typing import Dict

input_e = input()
unique_words: Dict[str, str] = OrderedDict() if version_info.minor < 7 else dict()

for word in input_e.split():
    lower_word = word.lower()

    if not lower_word in unique_words:
        unique_words[lower_word] = word

print(" ".join(unique_words.keys()))
