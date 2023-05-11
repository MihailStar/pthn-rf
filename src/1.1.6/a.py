# Задача A

from itertools import count


class PrimesIterator:
    def __init__(self, start: int = 2):
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        for integer in count(self._start):
            is_prime = True

            for divider in range(2, integer):
                if integer % divider == 0:
                    is_prime = False
                    break

            if is_prime:
                self._start = integer + 1
                return integer
