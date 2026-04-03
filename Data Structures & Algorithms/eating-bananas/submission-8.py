class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intuition is that we have to binary search the value k
        # which we compute from the maximum value in the pile
        # so we check to see if we can eat all bananas within the 
        # constraint and if we cannot, increase or decrease k accordingly
        # to get the tightest low bound
        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            tmp = h
            ct = 0
            for b in piles:
                if b - k <= 0:
                    ct += 1
                else:
                    ct += (b // k)
                    if b % k != 0:
                        ct += 1
                if ct > h:
                    break
            if ct > h:
                l = k + 1
            else:
                r = k - 1
        return l