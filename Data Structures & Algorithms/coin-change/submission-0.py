class Solution: # O(amount * len(coins)) time, O(amount) extra space
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unbounded knapsack - greedy approach doesnt work here
        # brute force - DFS / backtracking works if you prune invalid solutions and duplicates
        # as always, create a decision tree to visualize with DFS and see where solutions repeat
        # result is the minimum path length in the decision tree
        # store results in a cache/DP memo to avoid recomputing - TOP DOWN approach
        # may have worse space complexity due to recursive calls
        #
        # Actual DP / Bottom-up approach - tabulation starting at 0 coin value
        # still have to check each coin value to find the min coins required
        # technically still a brute force way
        dp = [float("inf")] * (amount + 1) # auxiliary array of N + 1 size
        dp[0] = 0

        for amt in range(1, amount + 1): # check each amount within the range, exclusive so need +1
            for coin in coins: # brute forcing so check each coin value
                if amt - coin >= 0:  # potential valid solution
                    # compare new possible solution to old one - this is the recurrence relation
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        if dp[amount] != float("inf"): # check if a valid solution even exists
            return dp[amount]
        return -1 # no solution