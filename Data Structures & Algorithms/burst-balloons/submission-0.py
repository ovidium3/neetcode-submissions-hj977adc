class Solution: # O(n^3) time, O(n^2) space
    def maxCoins(self, nums: List[int]) -> int:
        # at the very least, have a brute force approach where we run backtracking O(n^n)
        # subproblem - 2^n subproblems by checking each subarray to include / not include
        # even simpler - for n nums, at most n^2 subarrays. separate into 2 contiguous subarrays?
        # cant just look at subarrays independently. instead, consider popping value last.
        # if we pop last, subarrays will never be connected to each other, so we CAN pop independently
        # imagine that similar to the implicit '1' being there, the value in the middle is implicitly there.
        # 2D cache - indexed by L, R values indicating subarray
        # same brute force decision tree, just using a cache
        # modify input array adding implicit 1 to beginning and end
        # n^3 time since there are n^2 subarrays, and we have to iterate over every value once
        nums = [1] + nums + [1] # add implicit 1's to begin and end
        dp = {}

        def dfs(l: int, r: int) -> int:
            # base cases
            if l > r: # out of bounds
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
        
            dp[(l, r)] = 0
            for i in range(l, r + 1): # linear time loop if not cached already
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)

                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2) # since we modified array to include out of bounds 1s