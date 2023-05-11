# Задача H

words = input().split()
buttons = list(map(int, input()))

BUTTONS = [
    [],
    [],
    ["а", "б", "в", "г"],
    ["д", "е", "ж", "з"],
    ["и", "й", "к", "л"],
    ["м", "н", "о", "п"],
    ["р", "с", "т", "у"],
    ["ф", "х", "ц", "ч"],
    ["ш", "щ", "ъ", "ы"],
    ["ь", "э", "ю", "я"],
]

result = words

for index, button in enumerate(buttons):
    result = filter(
        lambda input_word: input_word[index].lower() in BUTTONS[button], result
    )

print(" ".join(result))
