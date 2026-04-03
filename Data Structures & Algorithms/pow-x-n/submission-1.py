class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1: # check curr bit --> if yes then multiply by x
                res *= x
            x *= x # square x for next iteration to possibly append to res
            power = power >> 1 # bit shift power over to check next bit
        # negative number means we have to invert result
        # since we cannot do the calculation with a fraction
        # just use property of division
        return res if n >= 0 else 1 / res