class Solution: # O(m * n) where m = len(s1), n = len(s2)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # seems pretty straightforward - but what if chars match?
        # we have to then dfs and try both paths - taking from s1 or s2 is its own path
        # use a 2D dp array to store bool of each position we can interleave up to, including out of bounds
        # s3 pointer will always be sum of s1 and s2 pointers
        if len(s1) + len(s2) != len(s3): # edge case: cannot possibly interleave
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)] # has to be 2D since diff paths exist
        dp[len(s1)][len(s2)] = True # base case, bottom right out of bounds will ALWAYS be true since youre comparing 2 empty chars
        for c1 in range(len(s1), -1, -1): # build dp table from the bottom right
            for c2 in range(len(s2), -1, -1): # so we have to iterate backwards through both strings
                c3 = c1 + c2
                if c1 < len(s1) and s1[c1] == s3[c3]: # s1 ptr is in bounds and chars match
                    if dp[c1 + 1][c2]: # mark current square as True if the one below it is True
                        dp[c1][c2] = True
                if c2 < len(s2) and s2[c2] == s3[c3]: # s2 ptr is in bounds and chars match
                    if dp[c1][c2 + 1]: # mark current square as True if the one to the right is True
                        dp[c1][c2] = True

        return dp[0][0]

        '''
        # memoization / recursive solution
        dp = {}

        # k = i + j
        def dfs(i: int, j: int) -> bool:
            # base cases
            if i == len(s1) and j == len(s2): # no more chars left to compare
                return True
            if (i, j) in dp: # already computed result
                return dp[(i, j)]
            
            # else continue dfs. need to check BOTH paths, just in case s1 and s2 chars both match
            k = i + j
            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j): # match from s1, continue dfs from next pos in s1
                return True
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1): # match from s2, continue dfs from next pos in s2
                return True
            
            # else we're done, stop dfs
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
        '''