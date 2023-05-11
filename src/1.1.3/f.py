# Задача F

from collections import defaultdict
from typing import DefaultDict, List

input_f = input()

temp: DefaultDict[str, List[str]] = defaultdict(lambda: [])

for word in input_f.split(" "):
    lower_word = word.lower()
    key = "".join(sorted(lower_word))

    temp[key].append(lower_word)

result = "\n".join(
    sorted(
        map(
            lambda words: " ".join(sorted(words)),
            filter(lambda words: len(words) > 1, temp.values()),
        ),
    )
)

print(result)
