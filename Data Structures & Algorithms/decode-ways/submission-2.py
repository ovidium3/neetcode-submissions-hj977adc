class Solution: # O(n) time AND space since auxiliary array OR stack
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 } # init dp table with 1 way at last index
        
        for i in range(len(s) - 1, -1, -1): # iterate over string from reverse
            if s[i] == "0": # no way to decode a leading 0
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 in range(len(s)) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2] # check two ahead
        return dp[0]

    '''
    # memoization DFS solution
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }
            
        def dfs(i):
            # base cases
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0 # no possible decoding for leading 0
                
            res = dfs(i + 1)
            if s[i] == "1" or s[i] == "2":
                if i + 1 in range(len(s)) and s[i + 1] in "0123456":
                    res += dfs(i + 2) # skip over two characters
            dp[i] = res
            return res
            
        return dfs(0)
    '''