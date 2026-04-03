class Solution: # O(m * n) time, O(n) mem, where n = amt and m = len(coins)
    def change(self, amount: int, coins: List[int]) -> int:
        # knapsack problem. combinations, NOT permutations so order doesnt matter
        # decision tree - one option to select from each coin. how to avoid duplicates?
        # have to restrict certain paths from using specific coin values
        # memoization top down - cache solutions with recursive DFS implementation
        # DP solution can reduce mem to O(n)
        # 2D grid with coin on left, amount on the top?
        # can instead compute one row at a time, with up to two rows in memory at any given moment
        # the idea is we will never look down more than one row at a time, but can look at the end of the row

        dp = [0] * (amount + 1) # O(n) memory to hold one row at a time
        dp[0] = 1 # 1 way to sum up to 0

        for coin in coins:  # Iterate through coins directly, no need to reverse
            for a in range(coin, amount + 1):  # Correct direction: left to right for each coin
                dp[a] += dp[a - coin]  # Add ways to form amount `a - coin`

        return dp[amount]

        '''
        # recursive solution - O(m * n) time AND space
        cache = {}

        def dfs(i, a):
            # base cases
            if a == amount: # target amount hit
                return 1
            if a > amount: # cannot possibly sum up to the amount
                return 0
            if i == len(coins): # index out of bounds - no more coins available
                return 0
            if (i, a) in cache: # already computed result, so take it from the cache
                return cache[(i, a)]
            
            # either choose coin or skip it
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        
        return dfs(0, 0)
        '''