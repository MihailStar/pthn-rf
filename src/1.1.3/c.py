# Задача C

input_c = input()


def compress(text: str) -> str:
    counter = 1
    compressed_text = ""

    for index, char in enumerate(text):
        try:
            next_char = text[index + 1]
        except IndexError:
            next_char = ""

        if char == next_char:
            counter += 1
        else:
            compressed_text += "{0}{1}".format(char, counter)
            counter = 1

    return compressed_text


print(compress(input_c))
