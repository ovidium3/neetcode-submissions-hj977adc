class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""

        pMax = min(strs)
        for i in range(len(pMax)):
            prev = strs[0][i]
            for s in strs:
                if s[i] != prev:
                    return prefix
            prefix += prev
        return prefix