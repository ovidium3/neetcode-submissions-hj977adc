class Solution:
    def findMin(self, nums: List[int]) -> int:
        # intuition: we can scan thru the
        # entire array binary searching, 
        # and since we know we will find the val
        # we can return lower bound once again
        # but this time with a classic l<r approach
        # checking against the right value. if the right 
        # value is smaller, then that means we are approaching
        # the correct ans
        if nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]