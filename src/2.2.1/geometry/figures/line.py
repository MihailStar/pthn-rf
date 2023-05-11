from math import sqrt

from geometry.point import Point


class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.points = (point_a, point_b)

    def __repr__(self) -> str:
        return "Line(%s, %s)" % self.points

    def length(self) -> float:
        """
        >>> Line(Point(0, 0), Point(0, 1)).length()
        1.0
        """

        point_a, point_b = self.points
        x_a, y_a = point_a.coord
        x_b, y_b = point_b.coord
        distance = sqrt(pow((x_b - x_a), 2) + pow((y_b - y_a), 2))

        return distance


__all__ = ["Line"]
