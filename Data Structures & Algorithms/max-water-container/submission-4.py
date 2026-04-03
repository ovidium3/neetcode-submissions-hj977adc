class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            lH, rH = heights[l], heights[r]
            curSum = min(lH, rH) * (r - l)
            res = max(curSum, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res