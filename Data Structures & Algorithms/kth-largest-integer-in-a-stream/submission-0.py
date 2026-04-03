class KthLargest: # O(n log(n)) worst case for init

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # copy it as an array for now, turn into a heap later
        self.k = k # size of min heap

        heapq.heapify(self.minHeap) # heapq.heapify() - heapq is a python module

        while len(self.minHeap) > self.k: # pop until reach desired size - could be up to O(n) times
            heapq.heappop(self.minHeap) # this is how you pop from heap in python - O(log(n))

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # this is how you push to heap in python - O(log(n))
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # edge case of minheap having less than k elts
        return self.minHeap[0] # min value always stored in the 0 index