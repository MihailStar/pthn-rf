from math import sqrt

from geometry.figures.line import Line
from geometry.point import Point


class Triangle:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.points = (point_a, point_b, point_c)

    def __repr__(self):
        return "Triangle(%s, %s, %s)" % self.points

    def aSide(self):
        point_a, point_b, _point_c = self.points

        return Line(point_a, point_b)

    def bSide(self):
        _point_a, point_b, point_c = self.points

        return Line(point_b, point_c)

    def cSide(self):
        point_a, _point_b, point_c = self.points

        return Line(point_a, point_c)

    def perimeter(self):
        """
        >>> Triangle(Point(0, 0), Point(0, 1), Point(1, 0)).perimeter()
        3.4142
        """

        length_a = self.aSide().length()
        length_b = self.bSide().length()
        length_c = self.cSide().length()
        P = length_a + length_b + length_c

        return round(P, 4)

    def square(self):
        """
        >>> Triangle(Point(0, 0), Point(0, 1), Point(1, 0)).square()
        0.5
        """

        half_perimeter = self.perimeter() / 2
        length_a = self.aSide().length()
        length_b = self.bSide().length()
        length_c = self.cSide().length()
        S = sqrt(
            half_perimeter
            * (half_perimeter - length_a)
            * (half_perimeter - length_b)
            * (half_perimeter - length_c)
        )

        return round(S, 4)


__all__ = ["Triangle"]
