class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif t == "-":
                minus = stack.pop()
                stack.append(stack.pop() - minus)
            elif t == "*":
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif t == "/":
                div = stack.pop()
                stack.append(int(float(stack.pop()) / div))
            else:
                stack.append(int(t))
                
        return stack[0]