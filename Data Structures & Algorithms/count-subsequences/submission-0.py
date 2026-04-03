class Solution: # O(n * m) time AND space
    def numDistinct(self, s: str, t: str) -> int:
        # have two ptrs, i and j, for each string.
        # option to increment both i and j if they match, OR just increment i
        # if they dont match, also just increment i
        # this can be done with DFS
        # base case is if t is empty, can take one empty substr from string s, so return 1
        # other base case is if s is empty, and t is not, return 0 since no subsequences exist

        cache = {}

        def dfs(sPtr: int, tPtr: int) -> int:
            # base cases
            if tPtr == len(t): # no more chars left to check from t
                return 1
            if sPtr == len(s): # nothing left to take from s
                return 0
            if (sPtr, tPtr) in cache: # DP to avoid computing same solution twice
                return cache[(sPtr, tPtr)]

            if s[sPtr] == t[tPtr]:
                cache[(sPtr, tPtr)] = dfs(sPtr + 1, tPtr + 1) + dfs(sPtr + 1, tPtr)
            else:
                cache[(sPtr, tPtr)] = dfs(sPtr + 1, tPtr)
            
            return cache[(sPtr, tPtr)]
        
        return dfs(0, 0)