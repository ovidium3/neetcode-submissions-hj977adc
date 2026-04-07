class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False # too many edges means that we must have a cycle somewhere
        
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n2].append(n1)
            adjList[n1].append(n2)

        # now we go thru the graph and try to see if
        # fast and slow ptrs intersect otherwise
        # if fast ptr reaches null then return F
        # starting at each node?
        # or we could start a BFS at node 0 and see
        # if we encounter any dupe values
        seen = set()

        bfs = deque()
        bfs.append([0, -1]) # store curr AND parent to avoid
        # doubling back

        while bfs:
            for i in range(len(bfs)):
                curr, parent = bfs.popleft()
                if curr in seen:
                    return False
                adj = adjList[curr]
                for a in adj:
                    if a != parent:
                        bfs.append([a, curr])
                
                seen.add(curr)
            
        return len(seen) == n # in case we didnt proc all nodes