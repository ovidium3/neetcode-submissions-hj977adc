class MyStack:
    # O(n) push operation. can make it O(1) by using q of queues
    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)
        # must append popleft to reorder the stack
        # since default behavior would remove from the wrong
        # end without built in queue behavior (cannot do)
        for _ in range(len(self.dq) - 1):
            self.dq.append(self.dq.popleft())

    def pop(self) -> int:
        return self.dq.popleft()

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()