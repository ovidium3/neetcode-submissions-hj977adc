class Solution: # O(E * alpha(V)-inverse ackermann func) time, O(V) space
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find algo (disjoint set union) - literally made for a problem like this
        # 2 arrays - parent array initially with each node being the parent of itself
        # forest of n trees. connecting nodes as you go, and maintain rank/size of each node component (init 1)
        # the rank thing is just an optimization - merge smaller component into the bigger one
        # union components who share the same root parent to minimize tree height.
        parent = [i for i in range(n)] # each node is the parent of itself
        rank = [1] * n

        def find(node):
            res = node

            while res != parent[res]: # go up the chain to find the ancestor
                parent[res] = parent[parent[res]] # path compression to set parent to grandparent as you go
                res = parent[res]
            
            return res
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2) # first want to find root parent of each node

            if parent1 == parent2:
                return 0 # no union necessary, already have the same ancestor
            
            # add smaller connected component to larger one
            if rank[parent2] > rank[parent1]: # parent 2 has larger component
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else: # parent 1 has larger component
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            return 1 # to indicate we did perform a successful union
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2) # decrement by 1 each time we perform a union
        
        return res # number of connected components
                
        '''
        # O(E + V) time and space, simple dfs search. works well for smaller graphs, not so much larger
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
        '''