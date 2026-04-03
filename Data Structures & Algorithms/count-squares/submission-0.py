class CountSquares:

    def __init__(self):
        self.pointMap = collections.defaultdict(int)

    def add(self, point):
        self.pointMap[(point[0], point[1])] += 1

    def count(self, point):
        pX, pY = point
        res = 0

        for x, y in self.pointMap:
            xDist, yDist = abs(pX - x), abs(pY - y)

            if xDist == yDist and xDist != 0:
                if (pX, y) in self.pointMap and (x, pY) in self.pointMap:
                    res += (self.pointMap[(x, y)] * self.pointMap[(x, pY)] * self.pointMap[pX, y])

        return res