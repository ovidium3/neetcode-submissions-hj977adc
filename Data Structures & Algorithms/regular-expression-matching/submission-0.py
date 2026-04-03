class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # . replaces a single char, * means char preceding can be repeated any number of times.
        # take 2^n decision tree and bring it down to O(n * m) top-down with cache OR bottom up DP
        # can turn top-down cache soln into actual dp solution bottom up
        # if star, can skip by doing (i, j + 2). else keep doing (i + 1, j) for each repeated char
        # if s[i] == p[j], do (i + 1, j + 1). if both i AND j out of bounds, perfectly matched.
        # if only j is out of bounds, do not match. if only i is out of bounds, can still match:
        # ex: s = a, p = a*b* so just bc i out of bounds, don't have to return False (edge case)
        # top-down memo approach

        def dfs(i: int, j: int) -> bool:
            # base cases
            if i >= len(s) and j >= len(p): # perfectly matched
                return True
            if j >= len(p): # no possible match
                return False

            # else keep checking further
            matchC = i < len(s) and (s[i] == p[j] or p[j] == ".") # check i in bounds first
            if (j + 1) < len(p) and p[j + 1] == "*": # star case(s)
                # check including * char or not. wrap multiline stuff ALL in parens
                return (dfs(i, j + 2) or            # don't use *
                        (matchC and dfs(i + 1, j)))  # use *
            
            if matchC: # chars match, check next idx
                return dfs(i + 1, j + 1)

            return False # default case of no match
        
        return dfs(0, 0)