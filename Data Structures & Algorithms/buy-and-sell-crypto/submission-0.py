class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        lowest = float('inf')

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            result = max(result, prices[i] - lowest)

        return result