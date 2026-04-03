class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                popped_h, popped_i = stack.pop()
                res = max(res, popped_h * (i - popped_i))
                start = popped_i

            stack.append([heights[i], start])
        
        for h, i in stack:
            res = max(res, h * (len(heights) - i))

        return res