class Solution: # O(E + V) time and mem, since creating adj list and traversing each once.
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # by definition, trees are not allowed to have loops AND every node needs to be connected
        # create an adjacency list using edges. empty graphs are valid by default, return True
        # can do BFS, but we'll do DFS. check for each node, visiting neighbors recursively
        # take num of input nodes and check if it matches visited nodes.
        # then check to make sure it does not contain any cycles, so keep a hashset of visited nodes
        #if not n: # base case - empty graph is a valid tree
        #    return True

        adjList = { i:[] for i in range(n) } # map of node to list of nodes, indicating adjacency
        for node1, node2 in edges: # populate adj list both ways since its UNdirected
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        visited = set() # contains current dfs path to check for any possible cycles
        def dfs(node: int, prev: int) -> bool:
            # base case
            if node in visited: # cycle detected
                return False
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor != prev: # dont run dfs on prev to avoid false positive cycle detection
                    if not dfs(neighbor, node): # cycle detected
                        return False
            return True # 

        return dfs(0, -1) and len(visited) == n # graph must be without cycles AND entirely connected