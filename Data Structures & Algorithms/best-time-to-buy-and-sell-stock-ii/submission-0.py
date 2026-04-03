class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            prev, curr = prices[i - 1], prices[i]

            if prev < curr:
                profit += curr - prev
        
        return profit