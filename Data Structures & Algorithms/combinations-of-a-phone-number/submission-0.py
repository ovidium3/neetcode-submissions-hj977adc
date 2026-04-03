class Solution: # O(3^n)
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitMap = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz",
                   } # small hashmap, not a big deal if we have to hardcode it

        def backtrack(i: int, curr: str) -> None:
            # base case - better than checking for i out of bounds
            if len(curr) == len(digits):
                res.append(curr) if len(curr) > 0 else None
                return
            
            currDigit = digits[i]
            for ch in digitMap[currDigit]:
                updatedCurr = curr[:] + ch
                backtrack(i + 1, updatedCurr)
        
        backtrack(0, "")
        return res