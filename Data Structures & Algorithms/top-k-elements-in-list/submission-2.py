import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # put pair in? 
            # since heap is list itll be list of pairs
            if len(heap) > k:
                heapq.heappop(heap) # only put top elts in heap
        
        res = []
        for i in range(k):
            res.append(heap[i][1]) # since they can be unordered, we dont need to pop from heap.

        return res