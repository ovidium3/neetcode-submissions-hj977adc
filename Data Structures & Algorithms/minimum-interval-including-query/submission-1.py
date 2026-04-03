class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        mappings = collections.defaultdict()
        i = 0
        minHeap = []

        sortedQueries = sorted(queries)
        for q in sortedQueries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                intLen = end - start + 1
                heapq.heappush(minHeap, (intLen, end))
                i += 1
            
            while minHeap and minHeap[0][1] < q: # smallest elt in min heap end before q start --> pop
                heapq.heappop(minHeap)
            if minHeap and minHeap[0][0]:
                mappings[q] = minHeap[0][0]
            else:
                mappings[q] = -1
        
        res = []
        for q in queries:
            if q in mappings:
                res.append(mappings[q])
            else:
                res.append(-1)

        return res
