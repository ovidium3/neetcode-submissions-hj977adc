class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # intuition: very similar to bananas problem
        # except in this case we can continue to iterate
        # over all the containers until we have fully 
        # loaded them. 
        # notice that L never dips below the maximum weight since
        # we cannot split a container into multiple pieces
        # and that the maximum constraint given 1 day
        # would be the entire sum of weights
        l, r = max(weights), sum(weights)

        if days == 1:
            return r

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