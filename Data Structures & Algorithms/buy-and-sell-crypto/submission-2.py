class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while r < len(prices):
            lo = prices[l]
            hi = prices[r]

            if lo < hi:
                res = max(res, hi - lo)
            else:
                l = r
            r += 1
        return res