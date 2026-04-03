class Solution: # O(n) time, O(1) mem
    def maxProduct(self, nums: List[int]) -> int:
        # decision tree - for each number, can brute force it and check each of n subarrays
        # we can do better using kadane's algo - positive/negative elements factor in to this
        # all positive is easy, just multiply all of them. negative sign switches so track min as well
        # edge case - value of 0 will "reset" streak - when encountering, resets max and min to 1 for multiplication reasons
        # still a DP problem, just maintaining 2 vals - currMin and currMax, no auxiliary array
        res = max(nums) # since all numbers could be negative so default of 0 wouldnt work
        currMin, currMax = 1, 1 # init at 1 to multiply with easier

        for n in nums:
            oldCurrMax = currMax # in case currMax gets overwritten, use old value for currMin calculation
            # 3 cases: pos * pos, neg * neg, or pos * neg
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * oldCurrMax, n * currMin, n)
            res = max(res, currMax)
        
        return res