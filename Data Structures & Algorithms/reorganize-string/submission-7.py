class Solution:
    def reorganizeString(self, s: str) -> str:
        # intuition: we can just check directly
        # if a character appears too many times
        # in a string and return early there
        # otherwise we KNOW we can build an interleaving
        # so we just build up a new string char by char
        # using a heap to process highest freq ones first
        # and if the freq ever hits 0 (since we simulate)
        # max heap by doing -1, we just dont add it back
        sCt = Counter(s)
        if max(sCt.values()) > (len(s) // 2) and len(s) % 2 == 0:
            # no possible way to deal with more than half
            # the chars being the same - return ""
            return ""
        elif max(sCt.values()) > (len(s) // 2) + 1 and len(s) % 2 == 1:
            return ""
        
        minHeap = [(-v, k) for k, v in sCt.items()]
        heapq.heapify(minHeap)

        res = [] # NOTE: always inefficent to build
        # a string from +=, just do "".join()
        while minHeap:
            freq, char = heapq.heappop(minHeap)
            if res and res[-1] == char:
                # need to pop next element and requeue this one
                newF, newC = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (freq, char))
                freq, char = newF, newC
            if freq < -1:
                # dont add back to heap if it is
                # the last time we would be using it
                heapq.heappush(minHeap, (freq + 1, char))
            res.append(char)
        
        return "".join(res)
