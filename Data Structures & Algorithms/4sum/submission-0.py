class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute force: quadruple nested loop
        # optimal: sort and do like 3 sum? but w extra loop?
        if len(nums) < 4:
            return []

        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    fixed = nums[i] + nums[j]
                    if fixed + nums[l] + nums[r] == target:
                        res.add(tuple((nums[i], nums[j], nums[l], nums[r])))
                        r -= 1
                        l += 1
                    elif fixed + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        return [list(r) for r in res]