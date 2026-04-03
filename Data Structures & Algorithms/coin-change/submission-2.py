class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: # no coins needed to make up 0
            return 0

        if min(coins) > amount: # smallest coin too big
            return -1
        
        dp = [float("infinity")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float("infinity") else -1
        # coins.sort()
        # coins.reverse()
        # res = 0
        # for c in coins:
        #     if c <= amount:
        #         while amount >= c:
        #             amount -= c
        #             res += 1
        # if amount == 0:
        #     return res
        # return -1