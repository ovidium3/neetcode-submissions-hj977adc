class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 # avoid edge case where empty input list
            
        res = 0
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(height[left], maxL)
                res += maxL - height[left]
            else:
                right -= 1
                maxR = max(height[right], maxR)
                res += maxR - height[right]


        return res
