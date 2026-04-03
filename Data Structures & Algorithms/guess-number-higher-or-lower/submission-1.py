# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # intuition: we want to narrow down on the 
        # search space of 1 to n so we start in the middle
        # and bsearch our way to the target which we are
        # guaranteed to return so we just inf loop til found
        l, r = 1, n
        while True:
            m = (l + r) // 2
            pick = guess(m)
            if pick == 0:
                return m
            elif pick == 1:
                l = m + 1
            else:
                r = m - 1