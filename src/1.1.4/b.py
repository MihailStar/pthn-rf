# Задача B

input_b = input()


def get_long_word(string: str) -> str:
    """Возвращает самое длинное слово в предложении"""

    sorted_words = sorted(string.split(), key=lambda word: len(word), reverse=True)

    return sorted_words[0]


print(get_long_word(input_b))
