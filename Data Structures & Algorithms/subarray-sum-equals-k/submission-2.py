class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # optimal solution: compute prefix sums O(n) time and space
        # but we do it as we iterate thru the elements
        # since we have base case of a 0 prefix sum
        # and check to see how many prefixes we can "chop off"
        # to achieve k from our current sum position
        prefix = defaultdict(int)
        prefix[0] = 1
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefix[diff]
            prefix[curSum] += 1
        
        return res
        
        
        # # brute force: n^2 time. doesnt even pass too inefficient
        # res = 0
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i, len(nums)):
        #         s += nums[j]
        #         if s == k:
        #             res += 1
        # return res