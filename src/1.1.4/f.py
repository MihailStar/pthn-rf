# Задача F

import re as regexp

input_f = input()


def isСorrect(password: str) -> bool:
    if (
        6 <= len(password) <= 12
        and regexp.search(r"[0-9]", password)
        and regexp.search(r"[A-Z]", password)
        and regexp.search(r"[a-z]", password)
        and regexp.search(r"[!@#$%^&*()_+]", password)
    ):
        return True

    return False


print(isСorrect(input_f))
