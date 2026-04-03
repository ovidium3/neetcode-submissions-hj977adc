class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # avoids issue of dealing w last temp being 0, just init all to 0
        stack = [] # contains pairs of [temp, index]

        for i, temp in enumerate(temperatures): # get curr index and temp at curr index
            while stack and temp > stack[-1][0]: # clear stack until new temp is no longer higher than last temp in stack
                sTemp, sIdx = stack.pop() # keep popping temps that are lower than newly added
                res[sIdx] = (i - sIdx) # update resulting index, calculated by taking curr index - index at which older temp occurred

            stack.append([temp, i]) # add each new temp to the stack to process in while loop

        return res