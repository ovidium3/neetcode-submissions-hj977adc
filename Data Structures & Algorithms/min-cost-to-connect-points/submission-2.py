class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # intuition: for each point, we want to 
        # find the closest point to it and connect them
        # adding that to our res
        # this is exactly what a MST is (Prim's / Kruskal's)
        adjList = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        
        res = 0
        mst = set()

        # now that we have the adj list built we 
        # can start building the MST
        minHeap = [[0, 0]] # store cost of getting to node i and its idx.
        # node 0 has 0 cost to get to
        while len(mst) < len(points): # keep building it
            cost, i = heapq.heappop(minHeap)
            if i in mst:
                continue
            res += cost # else add it and its cost to the MST
            mst.add(i)

            for neighborCost, neighbor in adjList[i]:
                if neighbor not in mst:
                    heapq.heappush(minHeap, [neighborCost, neighbor])
        
        return res
