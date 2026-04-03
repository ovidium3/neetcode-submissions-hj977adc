class Solution: # O(n^2) time, O(1) space since counting substrings, not tracking
    def countSubstrings(self, s: str) -> int:
        # must split into two cases this time
        res = 0
        for i in range(len(s)):
            # odd length palindrome substrings
            l, r = i, i
            while l in range(len(s)) and r in range(len(s)):
                if s[l] != s[r]: # chars no longer match
                    break
                res += 1 # new palindrome found
                l -= 1
                r += 1
                
            # odd length palindrome substrings
            l, r = i, i + 1
            while l in range(len(s)) and r in range(len(s)):
                if s[l] != s[r]: # chars no longer match
                    break
                res += 1 # new palindrome found
                l -= 1
                r += 1
        return res