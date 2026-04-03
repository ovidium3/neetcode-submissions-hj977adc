class Solution: # O(n) time AND mem since using auxiliary array OR stack space
    def climbStairs(self, n: int) -> int:
        # in dp, most important is to define the recurrence relation, as well as base cases
        # here, it is memo[i] = memo[i - 1] + memo[i - 2] (fibonacci sequence)
        # top down or bottom up approach - memoization is bottom up, recursion is top down
        # base cases - dont even need them since theyre auto initialized in memo array
        #if n <= 3:
        #    return n
        # else have to do a bit of recursion
        memo = [ i for i in range(n + 1) ] # start off by putting in base cases, and overwrite later values
        for i in range(3, n + 1): # start at index 3, or 4th position since 1-3 are already correctly filled in
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n] # since at n would be indexing out of bounds