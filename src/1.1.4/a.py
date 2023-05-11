# Задача A

input_a = input()
numbers = filter(bool, map(int, input_a.split()))


def get_average(*args: int) -> float:
    """Возвращает среднее арифметическое ненулевых аргументов"""

    if not args:
        return 0

    sum_of_args = sum(args)
    number_of_args = len(args)
    average = sum_of_args / number_of_args
    rounded_average = round(average)

    return rounded_average if rounded_average == average else average


print(get_average(*numbers))
