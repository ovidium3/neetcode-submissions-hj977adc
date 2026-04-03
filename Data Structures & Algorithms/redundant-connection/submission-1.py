class Solution: # O(n) using union find
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # can do a basic dfs in O(n^2), but with union find can do it in O(n)
        n = len(edges)
        parents = [i for i in range(n + 1)] # not actually gonna be using the 0 node, just makes math easier
        rank = [1] * (n + 1)

        def find(node: int) -> int: # returns index of ancestor node
            p = parents[node] # get current node parent to init

            while p != parents[p]: # while p is not equal to its own parent
                parents[p] = parents[parents[p]] # path compression - shorten link straight to grandparent
                p = parents[p]
            
            return p # now p == parents[p] so we found the top parent node, where it is equal to itself
        
        def union(node1: int, node2: int) -> bool: # returns if unioned successfully or not
            parent1, parent2 = find(node1), find(node2) # go up the heirarchy to find idxs of ancestors
            if parent1 == parent2: # nodes are already part of connected component
                return False
            # else find which parent has the higher rank, to add the smaller component to
            if rank[parent2] > rank[parent1]:
                # add parent1 component to parent2 component
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            else: # parent 1 component size is higher so add to that instead
                # add parent 2 component to parent 1 component
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            return True
        
        for node1, node2 in edges: # go through each connected pair of nodes and connect from start
            if not union(node1, node2): # if they are already connected, we have found the unnecessary link
                return [node1, node2] # there is always gonna be an extra node connection