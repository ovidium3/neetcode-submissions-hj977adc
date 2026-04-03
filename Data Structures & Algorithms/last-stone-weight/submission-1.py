class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # turn values all negative to make a max heap since python only has minheaps
        heapq.heapify(stones) # turn stones array into a max heap

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            secondHeaviest = heapq.heappop(stones)

            if heaviest != secondHeaviest: # consider non equal weights as equal weights both disappear
                newWeight = abs(heaviest - secondHeaviest)
                heapq.heappush(stones, -newWeight) # instead of doing conversions for each stone
                # convert newly formed stone into negative

        return 0 if not stones else -stones[0] # turn stone value back to positive if it exists