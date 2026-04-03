class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        for right in range(k, len(nums)):
            res.append(max(nums[left:right]))
            left += 1
        res.append(max(nums[left:len(nums) + 1]))

        return res
