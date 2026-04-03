class Solution: # O(n) time AND space
    def maxProfit(self, prices: List[int]) -> int:
        # 3 choices - buy/sell OR cooldown, which we can always do. still a binary decision tree
        # unfortunately this is O(2^n) BUT we can use caching to reduce to O(n)
        # cache key = index, with a bool for buy/sell
        dp = {} # key = {i, buying}, val = profit

        def dfs(i, buying):
            # base cases
            if i not in range(len(prices)):
                return 0
            if (i, buying) in dp: # already computed result
                return dp[(i, buying)]

            # handle buy/sell
            cooldown = dfs(i + 1, buying) # still an option regardless of in a buy or sell state
            if buying:
                buy = dfs(i + 1, not buying) - prices[i] # max profit in remaining array if we buy
                dp[(i, buying)] = max(buy, cooldown) # cache result as max of two decision trees
            else: # selling
                sell = dfs(i + 2, not buying) + prices[i] # max profit in remaining array if we sell
                dp[(i, buying)] = max(sell, cooldown) # same idea as above
            
            return dp[(i, buying)]
        
        return dfs(0, True)