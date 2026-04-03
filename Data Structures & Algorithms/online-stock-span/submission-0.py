class StockSpanner:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        res = 0
        while self.stack and self.stack[-1] <= price:
            self.stack2.append(self.stack.pop())
            res += 1
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)