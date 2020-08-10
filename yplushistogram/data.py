from __future__ import annotations
from typing import List

import bisect


class Face:
    def __init__(self, yplus: float, area: float):
        self._yplus = yplus
        self._area = area

    @property
    def yplus(self):
        return self._yplus

    @yplus.setter
    def yplus(self, newYplus):
        self._yplus = newYplus

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, newArea):
        self._area = newArea

    def __lt__(self, other: Face):
        return self.yplus < other.yplus

    def __repr__(self):
        return 'Area: ' + str(self._area) + ', yPlus: ' + str(self._yplus)


class FaceList(list):
    def __init__(self):
        super().__init__()

    def append(self, face: Face):
        bisect.insort(self, face)

    def countFacesInBand(self, from_: float, to_: float) -> int:
        i = bisect.bisect_left(self, Face(from_, -1))
        j = bisect.bisect_right(self, Face(to_, -1))
        return j - i - 1

    def band(self, from_: float, to_: float) -> List[Face]:
        i = bisect.bisect_left(self, Face(from_, -1))
        j = bisect.bisect_right(self, Face(to_, -1))
        return self[i:j]

    def surfaceArea(self) -> float:
        if not self:
            return 0.
        area = 0.
        for face in self:
            area += face.area
        return area

    def bandSurfaceArea(self, from_: float, to_: float) -> float:
        if not self:
            return 0.
        area = 0.
        for face in self.band(from_, to_):
            area += face.area
        return area

    def avgYplus(self) -> float:
        if not self:
            return 0.
        tot = 0.
        for face in self:
            tot += face.yplus
        return tot / len(self)
