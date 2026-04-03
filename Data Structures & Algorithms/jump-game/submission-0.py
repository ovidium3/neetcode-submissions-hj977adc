class Solution: # O(n) time, O(1) space
    def canJump(self, nums: List[int]) -> bool:
        '''
        # brute force - dfs decision tree testing up to nums[i] jumps so O(n^n), caching can do O(n^2)
        dp = [-1] * len(nums) # indicate unvisited

        def dfs(i: int) -> bool:
            # base cases
            if i >= len(nums) - 1: # reached last idx
                return True
            if nums[i] == 0: # cannot jump any more from here
                dp[i] = 0
                return False
            if dp[i] != -1: # visited already, avoid recomputing
                return dp[i] == 1 # True if path exists, False if path doesnt exist
            
            # else keep jumping forward
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    dp[i] = 1
                    return True

            dp[i] = 0
            return False
        
        return dfs(0)
        '''

        # greedy solution:
        # can also be solved using greedy algo to get constant time solution
        # this works because as long as the curr num is <= goalpost, can keep lowering the goalpost/target
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1): # dont even need to start from last, start from 2nd to last
            if i + nums[i] >= goal: # shift goalpost if we can reach it from curr pos
                goal = i

        return goal == 0 # if true, can reach goal from position zero