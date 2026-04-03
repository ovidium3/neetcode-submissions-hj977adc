class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force: start at 1 and just keep
        # guessing squares until val reaches threshold
        # of x then return val right before that
        # logn solution is to bsearch the entire range
        # up to x and narrow down
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1
        return r