class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # intuition: we can jsut set up a min heap
        # that contains pairing of shortest distance
        # and the point it corresponds to
        # since we alternatively could store a map for
        # these values but then it might get complicated
        # retrieving multiple values that might have the same
        # distance etc. this simplifies by sorting by min dist
        # running in O(n + k log n) time, O(n) space
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