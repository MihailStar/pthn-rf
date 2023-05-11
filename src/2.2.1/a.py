# Задача A

from geometry.figures.line import *
from geometry.figures.triangle import *
from geometry.point import *

print(Line(Point(0, 0), Point(0, 1)).length())
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)).perimeter())
print(Triangle(Point(0, 0), Point(0, 1), Point(1, 0)).square())
