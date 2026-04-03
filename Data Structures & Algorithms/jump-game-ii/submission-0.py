class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0

        l, r = 0, 0
        while r < len(nums) - 1:
            # jump to index of max val?
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            jumps += 1

        return jumps