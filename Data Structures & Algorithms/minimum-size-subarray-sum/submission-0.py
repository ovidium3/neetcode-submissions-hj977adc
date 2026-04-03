class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # intuition: one pass where we expand window til
        # it is valid, then shrink to where it is no longer valid
        # and keep going until hit end of array
        if sum(nums) < target:
            return 0
        if target == 1:
            return 1 # since all nums[i] guaranteed to be >= 1
        l, r = 0, 0
        res = 2**30
        curr = 0
        while r < len(nums):
            curr += nums[r]
            if curr >= target:
                #res = min(res, r - l + 1)
                # optimization: return if we found a single elt over tgt
                if res == 1:
                    return res
                while curr >= target:
                    curr -= nums[l]
                    l += 1
                res = min(res, r - l + 2)
            r += 1
        return res if res < 2**31 else 0