class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # init stack for parens
        res = [] # holds all valid output paren groupings

        # nested func to avoid passing in vars like n, stack, res
        def backtrack(openN: int, closedN: int) -> None:
            if openN == closedN == n: # if there are n open and n closing parens, add to res
                res.append("".join(stack)) # join all parens in stack using py str method

            if openN < n: # keep adding open parens until you cant anymore via recursive call
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # pop since stack acts as a global var

            if closedN < openN: # add closed parens until you cant anymore via recursive call
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # same as above pop

        backtrack(0, 0) # start backtracking with 0 as init
        return res