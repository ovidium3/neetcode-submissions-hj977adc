class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                summ = stack.pop() + stack.pop()
                stack.append(summ)
            elif t == "-":
                # NOTE: operand order - first pop is top
                # second pop is the second val, which we want to sub
                # from the top val we popped first.
                # same goes for division
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            elif t == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif t == "/":
                # truncate towards 0. 
                # do NOT use //, use / and int() conversion
                div = stack.pop()
                stack.append(int(stack.pop() / div))
            else:
                stack.append(int(t))

        return stack[0]