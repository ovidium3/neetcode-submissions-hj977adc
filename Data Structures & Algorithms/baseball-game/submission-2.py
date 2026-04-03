class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        # peek: stack[-1] is the top
        # push: stack.append()
        # pop: stack.pop() but dont do pop(0) since that
        # is O(n) time
        
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)