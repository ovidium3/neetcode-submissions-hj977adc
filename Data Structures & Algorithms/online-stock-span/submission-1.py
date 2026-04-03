class StockSpanner:
    # intuition: scan backwards every time and 
    # recompute how many times the stack[-1] is
    # less than current day's price
    # optimization: compress history
    # i.e. once a larger 

    def __init__(self):
        self.stack = [] # pair of price, ct
        # since the larger incoming value dominates

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)