class MedianFinder:

    def __init__(self):
        self.left = [] # max heap for left portion of sorted array
        self.right = [] # min heap for right portion of sorted array

    def addNum(self, num: int) -> None:
        # edge cases
        if not self.left and not self.right: # num is the first elt to be added
            self.left.append(-num)
            return
        if not self.right: # num is the second elt to be added
            leftNum = -self.left[0]
            if num < leftNum: # need to swap positions if second num is smaller than first
                self.left = [-num] # new left becomes array with just num in it
                self.right.append(leftNum) # new right becomes array with old left num
            else: # new num is larger so carry on
                self.right.append(num)
            return

        # extract values to determine which side to add to
        leftMax = -self.left[0]
        rightMin = self.right[0]

        if num > leftMax: # num belongs in right portion of array
            self.right.append(num)
            heapq.heapify(self.right)
        else: # num belongs in left portion of array
            self.left.append(-num)
            heapq.heapify(self.left)

        # finally, handle uneven list sizes
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right): # left side is bigger
                val = -heapq.heappop(self.left) # gotta convert back since right is a minHeap
                self.right.append(val) # add to right side
                heapq.heapify(self.right) # may be a more efficient way to do this
            else: # right side is bigger
                val = heapq.heappop(self.right)
                self.left.append(-val)
                heapq.heapify(self.left)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right): # even length, find mean of 2 middle vals
            leftMax, rightMin = -self.left[0], self.right[0] # top elt in heap is always at idx 0. - since left is maxHeap
            return (leftMax + rightMin) / 2
        elif len(self.left) > len(self.right): # left contains median
            return -self.left[0] # since it's a maxHeap
        return self.right[0] # else right contains median