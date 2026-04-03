class Solution: # O(E + V) time and space
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list and populate it
        adjList = { i:[] for i in range(n) }
        for node1, node2 in edges: # add to both adj lists since graph is UNdirected
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set() # track nodes in connected components to avoid running dfs on them again
        def dfs(node: int, prev: int) -> None:
            # base case
            if node in visited:
                return
            
            # add node to visited, and continue dfs
            visited.add(node)
            for i in adjList[node]:
                if i != prev: # avoid going back to dfs an already visited node
                    dfs(i, node)

        cc = 0 # count number of connected components
        for i in range(n):
            if i not in visited: # each time we find a new node, mark it and all connected to it as visited
                cc += 1
                dfs(i, -1) # init prev as -1 to indicate nonexistent since node >= 0
        return cc