class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(nums)
        realSum = 0
        for i in range(1, len(nums) + 1):
            realSum += i
        return realSum - n
        # MATH - calc diff between expected sum and what we got
        # fits time and space constraints
        # ALT SOLUTION - sort N log N time, constant space depending on the sorting algo