class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # could do this a DFS way, building up a prefix word from s until we get a word in the dict
        # then continuing until we get to the end of s. this would be O(n^2)
        # instead, we could just go through dict words and check if they match the first part of the string
        # this would be O(n*m*k) since we only check each char in s once, and m < n where m = word dict size, k = avg word length
        # but since we prune words that dont match at each step, it really is more efficient
        # increment i pointer by length of the word added each time. end once i == len(s)
        # want to cache points in decision tree where you return False as not possible to break down further, for future ref
        dp = [False] * (len(s) + 1) # since we index into len(s) at pos len(s) + 1
        dp[len(s)] = True # base case

        for i in range(len(s) - 1, -1, -1): # start at last index, decrement, end at idx -1 (exclusive)
            for w in wordDict:
                if (i + len(w) <= len(s) and # check if there are enough remaining chars in s to even compare
                    s[i : i + len(w)] == w): # and that part of s matches the word in the wordDict
                    dp[i] = dp[i + len(w)]
                if dp[i]: # == True, we have a promising path
                    break

        return dp[0]