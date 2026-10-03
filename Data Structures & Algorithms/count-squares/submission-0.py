class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)
        self.ptsL = []

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1
        self.ptsL.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.ptsL:
            if (abs(py-y) != abs(px-x)) or x == px or y == y == py:
                continue
            
            res += self.pts[(x,py)] * self.pts[(px,y)]
        return res