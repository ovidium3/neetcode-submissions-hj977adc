class MinStack:

    def __init__(self):
        # init a base array and a "min" array, keeping track of current min at each index
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # compare val from stack, if exists, to see if new val is a new low or not. if not append old
        if self.minStack and val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        # easy just pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # easy just return top of actual stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return top of min stack since it is keeping track of curr min value at the top
        return self.minStack[-1]
