class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # intuition: we can just track the curr max val
        # and the next val we see in the array
        # and compare that to see if we need to add
        # the curr max val or the new max when we expadn
        # the array using a hashmap

        if k == len(nums):
            maxNum = max(nums)
            return [maxNum]

        l, r = 0, k - 1
        res = []
        while r < len(nums):
            res.append(max(nums[l:r+1]))
            r += 1
            l += 1
        return res