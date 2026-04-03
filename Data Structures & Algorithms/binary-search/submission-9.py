class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        # NOTE: must do <= to avoid edge cases where
        # the last element of the array needs to be checked
        # and thus also need to set r to m - 1
        l, r = 0, len(nums) - 1
        if l == r:
            return 0 if nums[0] == target else -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1