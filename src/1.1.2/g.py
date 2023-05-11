# Задача G

input_g = input()


def cut(num: int) -> int:
    if num <= 9:
        return num

    sum_of_digits = sum(map(int, str(num)))

    return cut(sum_of_digits)


print(cut(int(input_g)))
