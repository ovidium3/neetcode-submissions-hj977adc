class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            left, right = s[l], s[r]
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            left = s[l]
            right = s[r]
            if s[l].isalpha():
                left = left.lower()
            if s[r].isalpha():
                right = right.lower()
            if left != right:
                return False
            l += 1
            r -= 1
        return True