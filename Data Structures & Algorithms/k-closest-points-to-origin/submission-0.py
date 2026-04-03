class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [] # init a min heap for distances made from points

        for x, y in points:
            dist = math.sqrt((x * x) + (y * y)) # euclidean distance formula. no abs needed since squaring
            heapq.heappush(dists, (dist, x, y)) # add dist to heap
        
        res = []
        for i in range(k):
            i, x, y = heapq.heappop(dists)
            res.append((x, y))

        return res