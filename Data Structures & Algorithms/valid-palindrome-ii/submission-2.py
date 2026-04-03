class Solution:
    def validPalindrome(self, s: str) -> bool:
        # optimal solution: branch when deleted char

        def isPalindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        deleted = False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if deleted:
                    return False
                deleted = True
                # break to two cases: move l or r ptr
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
        return True