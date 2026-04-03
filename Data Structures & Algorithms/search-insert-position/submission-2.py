class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # intuition: we are not doing a bsearch since 
        # we need to consider where to possibly insert this new
        # value, so we can narrow down using bsearch logic 
        # this is actually lower bound since we are doing
        # l <= r so that eventually when r < l, 
        # l is at hte position we would need to insert.
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return l # because when loop ends,
        # l + 1 == r + 1 which is the exact insertion spot