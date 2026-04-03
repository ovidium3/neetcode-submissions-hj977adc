class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        left = 0
        right = len(heights) - 1

        while left < right:
            # can also call max func instead of reassigning temp variable
            temp = (right - left) * min(heights[left], heights[right])
            if temp > maxArea:
                maxArea = temp

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
            
            temp = 0

        return maxArea