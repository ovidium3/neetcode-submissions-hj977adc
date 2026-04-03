class FreqStack:
    # brute force solution: use a hash map to 
    # initialize a count for each elt in the stack
    # and then pop according to that count
    # better approach: we can use several stacks
    # categorized by their frequency
    def __init__(self):
        self.stacks = defaultdict(list)
        self.counts = defaultdict(int)
        self.maxF = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.maxF = max(self.counts[val], self.maxF)
        self.stacks[self.counts[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxF].pop()
        if not self.stacks[self.maxF]:
            self.maxF -= 1
        self.counts[val] -= 1
        return val
            

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()