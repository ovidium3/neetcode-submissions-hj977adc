class FreqStack:

    def __init__(self):
        self.s1 = []
        self.aux = []
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        self.s1.append(val)

    def pop(self) -> int:
        maxF = max(self.freqs.values())
        while self.freqs[self.s1[-1]] != maxF:
            self.aux.append(self.s1.pop())
        tmp = self.s1.pop()
        self.freqs[tmp] -= 1
        while self.aux:
            self.s1.append(self.aux.pop())
        return tmp
            

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()