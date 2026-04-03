class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": # edge cases. second is necessary, first is a optimization
            return ""

        tCount = {} #init t string's map and window's map
        window = {}

        for c in t: # populate t string's map
            tCount[c] = 1 + tCount.get(c, 0)
        
        have = 0 # init have and need, indicating when character count conditions are met
        need = len(tCount)

        res = [-1, -1] # init result and result length, which is inf to indicate not possible
        resLen = float("infinity")

        left = 0
        for right in range(len(s)): # set up sliding window with l and r ptrs
            c = s[right]
            window[c] = 1 + window.get(c, 0) # extract curr char at right and add to window

            if c in tCount and window[c] == tCount[c]: # indicate when char count condition is met
                have += 1

            while have == need: # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)

                window[s[left]] -= 1 # pop from left of window
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1

                left += 1

        # result - return "" if no window found
        if resLen == float("infinity"):
            return ""

        return s[res[0]:res[1] + 1]
