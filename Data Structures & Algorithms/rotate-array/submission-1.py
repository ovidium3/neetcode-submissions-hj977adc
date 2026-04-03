class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force solution: iterate k times over array
        # optimization: do some kind of modulo to determine how
        # many times we really need to swap the array for
        if k == len(nums):
            return

        for i in range(k % len(nums)):
            popVal = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = popVal
