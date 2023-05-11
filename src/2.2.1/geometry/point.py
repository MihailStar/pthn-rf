from typing import Tuple, TypeAlias

Сoordinates: TypeAlias = Tuple[float, float]


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.coord: Сoordinates = (x, y)

    def __repr__(self) -> str:
        return "Point(%s, %s)" % self.coord


__all__ = ["Point"]
