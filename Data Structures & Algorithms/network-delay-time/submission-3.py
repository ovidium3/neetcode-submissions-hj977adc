class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # pure dijkstra since it is actually positive times
        # E log V works best with adj list and heap
        # shortest path graph algo
        # E is proportional to V ^ 2 since could have V edges for every V nodes
        # really E log V^2 -> 2 E log V -> E log V or V^2 log V
        adjList = defaultdict(list) # map edges
        for n1, n2, t in times:
            adjList[n1].append([n2, t])

        minHeap = [] # time, node
        minHeap.append([0, k])
        visited = set()
        res = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue # avoid dupe processing
            visited.add(node)
            res = max(res, time)

            for n2, t2 in adjList[node]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (time + t2, n2))

        return res if len(visited) == n else -1 # we cannot visit all nodes