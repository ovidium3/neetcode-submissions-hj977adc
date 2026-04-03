class Solution: # O(n^2) time
    def longestPalindrome(self, s: str) -> str:
        # brute force - could check every substring in O(n^3) time
        # since we would need a nested for loop AND checking palindrome
        # can reduce to checking each char, and for each char, running a two ptr solution for O(n^2)
        # edge case - checking even length palindromes
        res = ""
        for i in range(len(s)):
            count = 1 # count duplicates of char to determine if even or odd length palindrome substring
            j = i
            while j + 1 in range(len(s)) and s[j] == s[j + 1]:
                count += 1
                j += 1
            l, r = i, i + count - 1 # set to outermost valid spots
            
            curr = ""
            while l in range(len(s)) and r in range(len(s)): # guaranteed to iterate once successfully
                if s[l] != s[r]: # no longer palindromic
                    break
                curr = s[l:r + 1] # since left is inclusive, right is exclusive
                l -= 1 # have to move out l and r ptrs one more
                r += 1
            
            if len(curr) > len(res):
                res = curr
        return res