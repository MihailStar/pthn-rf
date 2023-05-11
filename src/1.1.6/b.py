# Задача B

# from __future__ import annotations


class ComplexNumber:
    def __init__(self, a: float, b: float) -> None:
        self._a = a
        self._b = b

    # def __add__(self, other: ComplexNumber) -> ComplexNumber:
    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            self._a + other._a,
            self._b + other._b,
        )

    # def __mul__(self, other: ComplexNumber) -> ComplexNumber:
    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            (self._a * other._a - self._b * other._b),
            (other._a * self._b + self._a * other._b),
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        return self._a == other._a and self._b == other._b
