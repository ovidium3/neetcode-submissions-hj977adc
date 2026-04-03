class Solution: # O()
    def minDistance(self, word1: str, word2: str) -> int:
        # can convert a char to no char, and no char to char in 1 op
        # base case: if one if them is empty, return len() of non-empty str
        # if the chars are equal, deal w subproblem of remaining strs (i + 1, j + 1)
        # else have 3 options: insert, delete or replace. so try all 3:
        # if insert, we increase len(word1) so check (i, j + 1)
        # if delete, we decrease len(word1) so check (i + 1, j)
        # if replace, we check subproblem of remaining strs (i + 1, j + 1)
        # for all 3 options, we have to increment ops by 1.
        # algo - 1 + table min(down, diag down, right)
        
        # row indexes into word1, col indexes into word2
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)] # w1 as row, w2 as col, w base case of 0
        for i in range(len(word2)): # fill last row with default values
            dp[len(word1)][i] = len(word2) - i
        for j in range(len(word1)): # fill last col with default values
            dp[j][len(word2)] = len(word1) - j

        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r + 1][c + 1], dp[r][c + 1])

        return dp[0][0]