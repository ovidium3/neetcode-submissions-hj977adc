class Solution:
    def isValid(self, s: str) -> bool:
        if s == "" or s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        pStack = []
        pDict = {']': '[', ')': '(', '}': '{'}

        for c in s:
            if c not in pDict:
                pStack.append(c)
            else:
                if not pStack or pDict[c] != pStack[-1]:
                    return False
                pStack.pop()

        return not pStack