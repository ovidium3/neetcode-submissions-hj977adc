class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # optimal solution: keep incrementing R
        # until we find a new val, then insert it
        insert, curr = 0, 0
        while curr < len(nums):
            nums[insert] = nums[curr]
            while curr < len(nums) and nums[curr] == nums[insert]:
                curr += 1
            insert += 1
        return insert