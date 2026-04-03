class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        numsMap = {}

        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in numsMap and i != numsMap[target - nums[i]]:
                return [i, numsMap[target - nums[i]]]