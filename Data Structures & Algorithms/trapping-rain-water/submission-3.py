class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        prefixL = [0] * len(height)
        prefixR = prefixL.copy()
        prefixL[0] = height[0]
        prefixR[-1] = height[-1]
        for i in range(1, len(height)):
            prefixL[i] = max(prefixL[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            prefixR[i] = max(prefixR[i + 1], height[i])
        
        mins = []
        for l, r in zip(prefixL, prefixR):
            mins.append(min(l, r))
        
        res = 0
        for i in range(len(height)):
            res += abs(height[i] - mins[i])
        return res