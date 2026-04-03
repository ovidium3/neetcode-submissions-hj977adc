class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # set up stack for numbers
        
        for t in tokens:
            if t == "+": # easy - pop last value and running total from stack, add em, push back on
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif t == "-": # tricky - save last popped val and sub from running total, push back on
                minus = stack.pop()
                stack.append(stack.pop() - minus)
            elif t == "*": # easy - pop last val and running total, mult, push back on
                mult = stack.pop() * stack.pop()
                stack.append(mult)
            elif t == "/": # tricky - save last popped val and div from running total using floor div
                div = stack.pop()
                stack.append(int(float(stack.pop()) / div)) # round to 0 using float trick
            else: # must be a num so push it on stack
                stack.append(int(t))
                
        return stack[0]