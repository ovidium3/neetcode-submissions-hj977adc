from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        tCt = Counter(t)
        currCt = Counter(s)
        for c in currCt.keys():
            currCt[c] = 0
        
        have, need = 0, len(tCt)
        res, resLen = [-1, -1], float("infinity")

        lo = 0
        for r in range(len(s)):
            c = s[r]
            currCt[c] += 1
            # filled req for another char
            if c in tCt and currCt[c] == tCt[c]:
                have += 1

            while have == need:
                if (r - lo + 1) < resLen:
                    res = [lo, r]
                    resLen = r - lo + 1

                currCt[s[lo]] -= 1
                # case where we remove one too many chars that we needed for req
                if s[lo] in tCt and currCt[s[lo]] < tCt[s[lo]]:
                    have -= 1 # effectively breaks loop
                lo += 1
        lo, r = res
        if res == float("infinity"):
            return ""
        return s[lo : r + 1]