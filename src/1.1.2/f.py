# Задача F
# @tutorial http://integrator.adior.ru/index.php/robototekhnika/242-python-fibonacci

input_f = input()


def fibonacci(index: int) -> int:
    f0 = 0
    f1 = 1

    for _i in range(index):
        f0, f1 = (f1, f0 + f1)

    return f0


print(fibonacci(int(input_f)))
