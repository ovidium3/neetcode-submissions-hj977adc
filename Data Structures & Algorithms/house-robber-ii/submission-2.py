class Solution: # O(n) time, O(n) space
    def rob(self, nums: List[int]) -> int:
        # same as first rob but added restriction of first and last being neighbors
        # use a helper func to check with first house, without last
        # AND option of without first house, with last
        # just compare with both versions of subarray
        return max(self.helper(nums[1:]), self.helper(nums[:-1])) if len(nums) > 1 else nums[0]

    def helper(self, nums): # reuse solution from house robber I
        for i in range(2, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3] if i > 2 else 0)
        return max(nums[-1], nums[-2]) if len(nums) > 1 else nums[0]