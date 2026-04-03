class Solution: # O(k log(n)) since we only pop k elts from heap in log n time
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [] # init a min heap for distances made from points

        for x, y in points:
            # dont even need to find sqrt since we dont have to return dist. just use it to compare
            dist = math.sqrt((x * x) + (y * y)) # euclidean distance formula. no abs needed since squaring
            dists.append((dist, x, y)) # dont heap push yet, that would be log(n) * n points == nlogn == sorting
            
        heapq.heapify(dists) # done in O(n) time by nature of heaps
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(dists) # heapify is sorted based on first elt in tuple only
            res.append((x, y))

        return res