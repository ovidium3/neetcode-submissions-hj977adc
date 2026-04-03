class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs_to_idxs = dict()
        for i, num in enumerate(nums):
            diffs_to_idxs[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs_to_idxs and i != diffs_to_idxs[diff]:
                return [i, diffs_to_idxs[diff]]
           
