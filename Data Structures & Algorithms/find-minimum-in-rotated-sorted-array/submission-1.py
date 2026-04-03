class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # set up left and right ptrs
        currMin = float("inf") # temp min val

        while l <= r:
            m = (l + r) // 2 # extract mid val
            currMin = min(currMin, nums[m]) # update currMin

            if nums[m] > nums[r]: # the min value lies to the right so move up left ptr
                l = m + 1
            else: # the min value lies in the left so move up right ptr
                r = m - 1
        return currMin#, nums[0]) # edge case where 