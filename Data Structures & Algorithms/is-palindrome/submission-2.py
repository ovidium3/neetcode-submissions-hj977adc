class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        lPtr = 0
        rPtr = len(s) - 1

        # ascii values - a = 97, A = 65. nums?

        while lPtr < rPtr:
            while lPtr < rPtr and not s[lPtr].isalnum():
                lPtr += 1
            while lPtr < rPtr and not s[rPtr].isalnum():
                rPtr -= 1
            if s[lPtr].lower() != s[rPtr].lower():
                return False
            
            lPtr += 1
            rPtr -= 1
            
        return True