class Solution: # O(n^2 log(n)) since n nodes mean n^2 edges, and log n to pop an edge from min heap
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST (minimum spanning tree) problem - prim's and kruskal's
        # prim's is better for dense graphs - O(V^2) with adj list or O((E + V) * log(V))
        # kruskal's is better for sparse graphs - O(E log(E)) since we're pre sorting edges
        # create and adjacency list, then use a min heap to implement prim's
        # connect every node together without forming a cycle - need n - 1 edges for n nodes
        # visited set to track nodes added, minHeap for nodes left to add (sorted by dist to add)
        # create adj list of point index mapped to distance from point at index to all other nodes
        nodes = len(points)
        adjList = { i:[] for i in range(nodes) }

        for i in range(nodes): # nested for loop to find dist from one node to ALL other nodes
            xi, yi = points[i]
            for j in range(i + 1, nodes): # avoid iterating over same point
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj) # extract distance between two points
                adjList[i].append([dist, j]) # add distance AND point to which the distance corresponds to
                adjList[j].append([dist, i]) # same thing for other point
        
        totalCost = 0
        visited = set()
        minHeap = [[0, 0]] # init with [0, 0] since distance from starting node to itself is 0
        while len(visited) != nodes: # or <, idea is while not all nodes have been visited yet
            dist, currNode = heapq.heappop(minHeap) # extract current node to process
            if currNode not in visited: # only process unvisited nodes to avoid cycles
                totalCost += dist # add distance to said node
                visited.add(currNode) # mark current node as now visited for future ref
                for cost, node in adjList[currNode]: # go through all remaining nodes and add dist from curr node to heap
                    if node not in visited: # only push unvisited nodes, theyll get filtered out anyway tho
                        heapq.heappush(minHeap, [cost, node])
        return totalCost