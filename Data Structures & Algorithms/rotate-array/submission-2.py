class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force solution: iterate k times over array
        # optimization: do some kind of modulo to determine how
        # many times we really need to swap the array for
        # final solution: swap in-place to final position
        n = len(nums)
        if k == n:
            return

        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
