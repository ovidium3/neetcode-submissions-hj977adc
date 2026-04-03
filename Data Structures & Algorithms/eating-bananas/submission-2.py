class Solution: # O(log(max(piles)) * piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need to iterate through each possible k value from 1 to the maximum value in piles.
        minK, maxK = 1, max(piles) # k value range / eating rate ranges from 1 to max val in piles
        res = maxK # init to worst case scenario - k value is largest value in piles

        while minK <= maxK: # classic binary search condition
            eatRate = (minK + maxK) // 2 # start with middle k value from possible list of kValues

            time = 0
            for bananas in piles:
                time += math.ceil(bananas / eatRate)

            if time <= h: # update result eating rate AND shift down right ptr, could be better solution
                res = eatRate
                maxK = eatRate - 1 # -1 to skip mid value you already tested just now
            else: # shift up left ptr, too narrow of a constraint
                minK = eatRate + 1 # again +1 since you skip over curr mid value you already tested

        return res