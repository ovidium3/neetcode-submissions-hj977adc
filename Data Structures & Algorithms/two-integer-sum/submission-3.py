class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in numsMap and i != numsMap[target - nums[i]]:
                return [i, numsMap[target - nums[i]]]