class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            # if nums[i] == 0, not, dont move goal.

        if goal == 0:
            return True
        return False