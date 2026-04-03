class Solution: # O(n) time, O(1) space with modifying nums in-place
    def rob(self, nums: List[int]) -> int:
        # sounds like a 0/1 knapsack problem
        for i in range(2, len(nums)):
            # avoid indexing out of bounds if i == 2, and NOT grab last value in nums
            nums[i] += max(nums[i - 2], nums[i - 3] if i > 2 else 0)
        # edge case if only one elt, else compare last two sums
        return max(nums[-1], nums[-2]) if len(nums) > 1 else nums[0]