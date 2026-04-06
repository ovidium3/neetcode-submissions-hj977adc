class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # condition: cannot exceed either threshold of
        # a, b, c AND cannot have more than two of a kind
        # next to one another
        # AND only use a, b, c
        maxHeap = []
        if a != 0:
            maxHeap.append([-a, "a"])
        if b != 0:
            maxHeap.append([-b, "b"])
        if c != 0:
            maxHeap.append([-c, "c"])
        if not maxHeap:
            return ""
        heapq.heapify(maxHeap) # always O(3) = constant time n space
        res = []

        # soon as we hit only one char left we cannot possibly interleave
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break # cannot add new chars anymore, break and return res
                newF, newC = heapq.heappop(maxHeap) # need to use next char in line
                res.append(newC)
                if newF < -1:
                    heapq.heappush(maxHeap, [newF + 1, newC])
                
                heapq.heappush(maxHeap, [freq, char])
            else:
                res.append(char)
                if freq < -1:
                    heapq.heappush(maxHeap, [freq + 1, char])

        return "".join(res)