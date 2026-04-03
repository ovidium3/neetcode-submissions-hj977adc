class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # contains pairs of [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                sTemp, sIdx = stack.pop()
                res[sIdx] = (i - sIdx)

            stack.append([temp, i])

        return res