class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
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