class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # intuition: greedily approach this
        # by sorting based on the earliest start time?
        # ensuring that there is no overlap
        # can either sort or use a heapify approach
        # then pop from the heap to get slightly better than
        # n log n time? in case we return early dont have to
        # fully process n iterations as if we sort it would be hard n log n
        # but in this case could be like n / 2 log n or smth
        trips.sort(key = lambda x: x[1])
        minHeap = []
        currPass = 0

        for p, start, end in trips:
            # remove finished trips
            while minHeap and minHeap[0][0] <= start:
                e, passengers = heapq.heappop(minHeap)
                currPass -= passengers

            # add current trip
            currPass += p
            if currPass > capacity:
                return False

            heapq.heappush(minHeap, (end, p))

        return True
        