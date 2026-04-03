class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
            
        pMap = {']': '[', '}': '{', ')': '('}

        stack = []

        for i in range(len(s)):
            if s[i] == "[" or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
                continue
            
            if not stack or stack[-1] != pMap[s[i]]:
                return False;
            stack.pop()

        return not stack
