class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(nlogn) brute force sort
        nums.sort()
        curr = 0
        for n in nums:
            if n < 1:
                continue
            if n - curr == 0:
                continue
            if n - curr == 1:
                curr += 1
            else:
                return curr + 1
        return curr + 1