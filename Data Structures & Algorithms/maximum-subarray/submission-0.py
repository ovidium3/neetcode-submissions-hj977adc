class Solution: # O(n) time, O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force - calculate each possible subarray in O(n^2) time
        # how to optimize even more - kadane's algo to run in O(n) time
        # if prefix is a negative sum, remove it. kinda like a sliding window.
        
        res = nums[0] # array has at least 1 elt

        currSum = 0
        for n in nums:
            currSum += n
            res = max(res, currSum) # update subarray

            if currSum < 0: # reset if at any point negative
                currSum = 0
        
        return res