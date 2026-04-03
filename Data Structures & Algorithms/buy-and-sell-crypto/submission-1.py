class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0  # buy
        right = 1 # sell
        
        while right < len(prices):
            if prices[left] < prices[right]:
                maxP = max(maxP, prices[right] - prices[left])
            else:
                left = right # update left ptr to become right ptr since it is new lowest
            right += 1

        return maxP