"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # can also run this check at the end when returning cloneDFS, this is for clarity only
            return None

        oldToNew = {} # map old nodes to new, copy nodes

        # recursively clone all nodes
        def cloneDFS(node: Optional['Node']) -> Optional['Node']:
            # base case
            if node in oldToNew: # we already copied the node, so just return the copy
                return oldToNew[node]
            
            # else we need to copy the node
            copy = Node(node.val)
            oldToNew[node] = copy

            # now need to recursively copy each neighboring node
            for neighbor in node.neighbors:
                copy.neighbors.append(cloneDFS(neighbor))
            return copy

        return cloneDFS(node) # this returns head of new adj list
        # dont even need to return oldToNew[node] can just do it directly