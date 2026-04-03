class Solution: # O(len(text1) * len(text2)) time and space since bottom up table
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # brute force DFS - find every possible subsequence and out of that, longest common
        # by default, longest possible length is min(text1, text2)
        # DP approach would be to create a 2D grid to track at each character of the string,
        # fill current square with max of what is to the right or down
        # RR is max(dp[r+1][c], dp[r][c+1]), +1 if strings at indices match
        # initialize outer bottom right half-perimiter with values of 0

        # text1 = row, text2 = col
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)] # since we need outer default row of 0s

        # fill dp table from right to left, bottom up
        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):
                dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]

        return dp[0][0] # result lies at top left