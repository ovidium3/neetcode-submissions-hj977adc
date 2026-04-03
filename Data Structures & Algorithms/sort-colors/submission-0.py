class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1


        # valid solution - two O(n) passes with O(1) space
        # cts = Counter(nums)
        # for i in range(len(nums)):
        #     if cts[0] > 0:
        #         nums[i] = 0
        #         cts[0] -= 1
        #     elif cts[1] > 0:
        #         nums[i] = 1
        #         cts[1] -= 1
        #     else:
        #         nums[i] = 2
