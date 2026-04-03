class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) time + space: only check possible lengths for 
        # starts of sequences, since it can be sequence
        # that is OUT OF ORDER we can use a set
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