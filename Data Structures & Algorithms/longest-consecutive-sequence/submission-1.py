class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        res = 0
        nums = set(nums)
        for n in nums:
            if n - 1 not in nums:
                curr = n
                tmp = 0
                while curr in nums:
                    tmp += 1
                    curr += 1
                res = max(res, tmp)
        
        return res