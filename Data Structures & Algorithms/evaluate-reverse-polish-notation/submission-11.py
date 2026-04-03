class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                summ = stack.pop() + stack.pop()
                stack.append(summ)
            elif t == "-":
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            elif t == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif t == "/":
                div = stack.pop()
                stack.append(int(stack.pop() / div))
            else:
                stack.append(int(t))

        return stack[0]