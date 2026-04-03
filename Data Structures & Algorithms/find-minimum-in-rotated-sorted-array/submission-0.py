class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # set up left and right ptrs
        currMin = float("inf") # temp min val

        while l <= r:
            m = (l + r) // 2 # extract mid val
            currMin = min(currMin, nums[m]) # update currMin

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(currMin, nums[0])