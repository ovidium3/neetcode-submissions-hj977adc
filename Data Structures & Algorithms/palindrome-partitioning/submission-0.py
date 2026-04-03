class Solution: # O(2^n)
    def partition(self, s: str) -> List[List[str]]:
        # brute force - backtracking by checking every single possible variation
        # only add to res if theyre palindromes
        res = []

        curr = []
        def dfs(i):
            # base cases
            if i >= len(s): # no more characters to check
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j): # call helper func to check palindrome from indices i to j
                    curr.append(s[i:j+1]) # +1 since end range is default exclusive
                    dfs(j + 1) # keep running dfs to look for addl partitions
                    curr.pop() # once were done with dfs, reset current partition for next search
        
        dfs(0)
        return res

    def isPali(self, s, l, r): # probably some lc easy subproblem here
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True