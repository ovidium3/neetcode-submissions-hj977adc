class Solution: # O(len(tasks) * n) time and O(n) mem, since push and pop is O(log26) NOT O(log(n))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks) # create a hashmap of chars mapped to frequencies
        maxHeap = [-count for count in freq.values()] # only want values (freqs). negate vals for max heap
        heapq.heapify(maxHeap)

        time = 0 # build result here
        q = deque() # queue of pairs containing freq, and time when itll be available

        while maxHeap or q: # process while pulling from heap OR queue, so no values remain unprocessed
            time += 1 # increment time passed

            if maxHeap: # check top freq value on heap
                count = 1 + heapq.heappop(maxHeap) # add 1 since were dealing with - values, so they get closer to 0 by adding instead of subbing
                if count: # if count is nonzero
                    q.append([count, time + n]) # add idle time n to indicate next availability
            
            if q and q[0][1] == time: # if queue has stuff in it and the idle time limit is up:
                queueVal = q.popleft()[0] # extract freq value from queue
                heapq.heappush(maxHeap, queueVal) # push it back on the heap to process again later

        return time