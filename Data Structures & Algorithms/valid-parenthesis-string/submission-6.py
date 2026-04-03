class Solution:
    def checkValidString(self, s: str) -> bool:
        minL, maxL = 0, 0
        for c in s:
            if c == "(":
                minL += 1
                maxL += 1
            elif c == ")":
                minL -= 1
                maxL -= 1
            else:
                minL -= 1
                maxL += 1
            if maxL < 0:
                return False
            elif minL < 0:
                minL = 0
        return minL == 0
        





        # if len(s) == 1:
        #     return s == "*"

        # stack = []
        # starStack = []
        # for i in range(len(s)):
        #     c = s[i]
        #     if c == "(":
        #         stack.append(i)
        #     elif c == ")":
        #         if not stack and not starStack:
        #             # no possible match for ')'
        #             return False
        #         if stack:
        #             stack.pop()
        #         else:
        #             starStack.pop()
        #     else:
        #         starStack.append(i)

        # # Try to match remaining '(' with '*' acting as ')'
        # while stack:
        #     if not starStack:
        #         return False

        #     left_index = stack.pop()
        #     star_index = starStack.pop()

        #     if star_index < left_index:
        #         return False

        # return True
        