class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for p in points:
            x2, y2 = p
            dist = math.sqrt((x2)**2 + (y2)**2)
            distances.append([dist, p])

        heapq.heapify(distances)
        res = []
        for i in range(k):
            dist, p = heapq.heappop(distances)
            res.append(p)
        return res