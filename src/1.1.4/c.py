# Задача C
# @tutorial https://thecode.media/leet-substring

input_c = input()


def get_longest_substring(string: str) -> str:
    """Возвращает самую длинную неповторяющуюся подстроку"""

    longest = ""
    temporary = ""

    for char in input_c:
        if char not in temporary:
            temporary += char
            longest = longest if len(longest) >= len(temporary) else temporary
        else:
            indexExisting = temporary.index(char)
            temporary = temporary[indexExisting + 1 :] + char

    return longest


print(get_longest_substring(input_c))
