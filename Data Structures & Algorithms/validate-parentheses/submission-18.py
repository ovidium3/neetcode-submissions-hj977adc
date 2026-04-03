class Solution:
    def isValid(self, s: str) -> bool:
        # optional base cases
        if s == "" or s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        pStack = [] # setup stack (list)
        pDict = {']': '[', ')': '(', '}': '{'} # create dict mapping of close parens to open

        for c in s: # iterate thru string
            if c not in pDict: # keep adding to stack as long as theyre open strings
                pStack.append(c)
            else: # pop from stack and make sure it corresponds to dict paren mapping
                if not pStack or pDict[c] != pStack[-1]: # case where stack empty or invalid elt on stack
                    return False
                pStack.pop() # remove last elt from stack after checking

        return not pStack # edge case where stack could still have elts, for ex. all open parens