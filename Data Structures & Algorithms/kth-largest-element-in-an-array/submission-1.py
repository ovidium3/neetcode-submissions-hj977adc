class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force: sort in reverse, and just 
        # go until we find the k-th element and return that
        # entire algo is TWO LINES:
        # nums.sort(reverse=True)
        # return nums[k - 1]
        #
        # optimal: use a maxHeap to heapify all the nums
        # then pop until we hit the desired number
        # trick is to negate the nums in heap 
        # so that we can simulate a max heap
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        # pop until we know next top elt is the k-th largest
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0] # dont forget to flip sign
