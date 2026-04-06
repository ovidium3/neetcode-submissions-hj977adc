class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # brute force: try to create a fixed array
        # interleaving all tasks without violating n cd time
        # could do a hashmap of all unique tasks, their ct
        # and cd left?
        # idea: max heap tracking most frequent element
        # simulated on minheap by having a negative frequency ct
        if n == 0:  # no cd, no problem
            return len(tasks)
        
        taskCt = Counter(tasks) # freq mapping of task : ct
        maxHeap = [-ct for ct in taskCt.values()] # negative freq to simulate max
        heapq.heapify(maxHeap)
        q = deque()
        
        time = 0
        while maxHeap or q: # since we need to add back to max heap from q
            time += 1

            if not maxHeap:
                time = q[0][1] # quick way to speed up time to process to next thing in heap
            else:
                ct = 1 + heapq.heappop(maxHeap) # get highest freq and decrement it (since it is stored as neg)
                if ct != 0:
                    q.append([ct, time + n]) # push it back on the queue with the new time it will be available to use
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time # finished procesing all q elts