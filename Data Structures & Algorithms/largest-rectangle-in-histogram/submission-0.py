class Solution: # O(n) time, O(n) space
    # start from left, and check how far you can "extend" a height - until encountering a lower elt
    # still have to compute areas after finding all valid index ranges that extend - keep track of max
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (index, height) since we pop from top after no longer considering elt

        for i, h in enumerate(heights):
            start = i
            # while stack not empty and top of stack is greater than height we just reached
            # have to pop stack AND check max rect we can create from popped height AND have to extend backwards
            while stack and stack[-1][1] > h:
                index, height = stack.pop() # since it is a pair
                maxArea = max(maxArea, height * (i - index)) # 
                start = index # extend backwards since this is greater height than we're visiting
            stack.append((start, h))
        
        # any remaining stack entries can be extended to end - all ascending order presumably
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea