class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)