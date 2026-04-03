class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(nums)
        realSum = 0
        for i in range(1, len(nums) + 1):
            realSum += i
        return realSum - n