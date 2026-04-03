class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjMap = {} # map source to dest and weight

        for i in range(n):
            adjMap[i] = []

        for s, d, w in edges:
            adjMap[s].append([d, w])

        shortestMap = {} # map vertex to shortest dist

        minHeap = [[0, src]]    #init with source node - dist of zero to itself
        while minHeap:  # run breadth first search (bfs)
            w1, v1 = heapq.heappop(minHeap) # pop from heap
            if v1 in shortestMap:
                continue # already found shortest so no need to keep searching for that node
            shortestMap[v1] = w1

            for v2, w2 in adjMap[v1]:
                if v2 not in shortestMap: # no point adding if already in
                    heapq.heappush(minHeap, [w1 + w2, v2])

        for i in range(n): # fill unreachable nodes with -1
            if i not in shortestMap:
                shortestMap[i] = -1

        return shortestMap