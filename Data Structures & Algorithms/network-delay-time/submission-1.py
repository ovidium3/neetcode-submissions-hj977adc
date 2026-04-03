class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # given a bunch of directed edges and positive weights (times) - assemble graph using dijkstra's
        # use priority queue
        # create adjacency list of nodes - more restrictive, since directed graph
        adjList = { i:[] for i in range(1, n + 1) } # n nodes, n adj lists
        for u, v, t in times: # populate adj list
            adjList[u].append((t, v)) # put time first since thats what we sort by.
        
        total = 0
        visited = set() # avoid processing same node multiple times
        pq = [[0, k]] # init with starting node and 0 time to get there
        while pq:
            runningTotal, currNode = heapq.heappop(pq)
            if currNode not in visited: # only process unvisited nodes
                visited.add(currNode)
                total = runningTotal

                for time, node in adjList[currNode]:
                    heapq.heappush(pq, [time + runningTotal, node])

        return total if len(visited) == n else -1