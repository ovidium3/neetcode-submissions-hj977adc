class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        seen = set()
        components = 0

        def gatherComponents(n):
            bfs = deque()
            bfs.append([n, -1])
            while bfs:
                curr, parent = bfs.popleft()
                if curr in seen:
                    continue
                adj = adjList[curr]
                for a in adj:
                    if a == parent:
                        continue
                    bfs.append([a, curr])
                seen.add(curr)

        for i in range(n):
            if i in seen:
                continue
            gatherComponents(i)
            components += 1
            
        return components