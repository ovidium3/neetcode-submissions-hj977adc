class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        x = x**n
        return x