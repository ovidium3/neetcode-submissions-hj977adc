class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since heaps are min heap by default, we
        # want to simulate a max heap
        # so we just negate every number
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            big1 = abs(heapq.heappop(stones))
            big2 = abs(heapq.heappop(stones))

            res = abs(big2 - big1)
            if res != 0:
                heapq.heappush(stones, res * -1) # put result back on heap
            # else we just destroy both stones, dont put any back

        # if we have one stone left, return it
        # otherwise just return 0
        return abs(stones[0]) if stones else 0