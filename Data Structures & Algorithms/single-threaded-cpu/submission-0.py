class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # store in min heap with the earliest available
        # start time as the invariant, as well as the 
        # shortest processing time
        # also need to factor in smallest index?
        # n log n time, n space
        tasks_with_index = []
        for i, (et, pt) in enumerate(tasks):
            tasks_with_index.append((et, pt, i))

        tasks = sorted(tasks_with_index) # enqueue time, processing time, index
        res = []
        minHeap = [] # shortest processing time, index
        time = 0
        i = 0

        while i < len(tasks) or minHeap:
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]

            # add all possible tasks to start on now
            # ordered by shortest proc time, index
            while i < len(tasks) and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(minHeap, (pt, idx))
                i += 1

            pt, idx = heapq.heappop(minHeap)
            time += pt
            res.append(idx) # process current task,
            # bump time up how long it took
        return res