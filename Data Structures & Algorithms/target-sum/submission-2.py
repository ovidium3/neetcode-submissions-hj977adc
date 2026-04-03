class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for num in nums, can either take + or - version of that num
        # this 2^n decision tree can be made more optimal by using caching and dfs
        # that you can then convert into a 2d memo table
        # this is a 0/1 knapsack problem - 

        cache = {} # map (idx, target) to num of unique ways

        def dfs(i: int, currSum: int) -> int:
            # base cases
            if i == len(nums): # no more nums to sum, so we either found a path or we didnt
                return 1 if currSum == target else 0
            if (i, currSum) in cache: # no need to recompute
                return cache[(i, currSum)]

            # else keep dfs'ing, counting ways in left positive subtree AND right negative subtree
            cache[(i, currSum)] = dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
            
            return cache[(i, currSum)]
        
        return dfs(0, 0)