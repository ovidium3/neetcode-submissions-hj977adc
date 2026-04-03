class Solution:
    def trap(self, height: List[int]) -> int:
        # optimal solution: track current highest L and R
        # O(n) time O(1) space
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res

        # # good solution: prefix maximums to find
        # # the mins of those, then we can iterate over array
        # # a 3rd time to comp how much we can add
        # # O(4n) -> O(n) time and O(2n) -> O(n) space
        # # can modify to improve space / time comp constants but
        # # this is essentially correct
        # if len(height) <= 2:
        #     return 0

        # prefixL = [0] * len(height)
        # prefixR = prefixL.copy()
        # prefixL[0] = height[0]
        # prefixR[-1] = height[-1]
        # for i in range(1, len(height)):
        #     prefixL[i] = max(prefixL[i - 1], height[i])
        # for i in range(len(height) - 2, -1, -1):
        #     prefixR[i] = max(prefixR[i + 1], height[i])
        
        # mins = []
        # for l, r in zip(prefixL, prefixR):
        #     mins.append(min(l, r))
        
        # res = 0
        # for i in range(len(height)):
        #     res += abs(height[i] - mins[i])
        # return res