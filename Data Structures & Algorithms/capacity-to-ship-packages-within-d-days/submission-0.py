class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l <= r:
            m = (l + r) // 2
            days_used = 1
            curr = 0

            for w in weights:
                if curr + w > m:
                    days_used += 1
                    curr = 0
                curr += w
            if days_used <= days:
                r = m - 1
            else:
                l = m + 1
        return l