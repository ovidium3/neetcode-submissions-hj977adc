class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # intuition: we can create a stack that contains
        # only numbers that can advance all the way thru
        # to the end, i.e. 1,3,2,4 would result in stack of
        # 1, 2, 4 since 3 wouldnt be able to advance bc of 2
        # in front of it.
        # store starting indices s.t. we can quickly calc
        # to figure out how long to "advance"
        # each bar in the stack when performing res area calcs
        
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