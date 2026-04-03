class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
        
        res = []
        for i in range(len(minHeap)):
            res.append(heapq.heappop(minHeap))
        return res