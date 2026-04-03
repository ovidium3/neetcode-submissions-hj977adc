# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # O(n) time (visit each node once) and O(h) space (as many stack frames as tree height)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # don't even need a helper func can just do it all in one
        if not root:
            return 0 # base case of null node
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # recursive DFS

    '''
    alt solution: iterative DFS - implement ***pre-order*** DFS with stack
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node: # won't actually use null nodes, just ignore them
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return res
    '''


    '''
    another solution: iterative BFS using queue
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level
    '''