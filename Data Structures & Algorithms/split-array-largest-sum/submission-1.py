class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # intuition: we can start by determining
        # how to group elements contiguously
        # by merge sorting them s.t. we minimize the total
        # sum when merging
        # wrong. we can do DP or some kind of backtracking
        # but ultimately the solution is bsearch
        l, r = max(nums), sum(nums)
        if k == len(nums):
            return l # since by default, largest sum in subarray = largest individual val

        res = r
        while l <= r:
            m = l + (r - l) // 2

            curSum = 0
            maxSum = 0
            cts = 1
            for i in range(len(nums)):
                #maxSum = max(maxSum, curSum)
                curSum += nums[i]
                if curSum > m:
                    curSum = nums[i]
                    cts += 1
                maxSum = max(maxSum, curSum)
                if cts > k:
                    break
            if cts <= k:
                r = m - 1
                res = maxSum
            else:
                l = m + 1

        return res