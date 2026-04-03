# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = defaultdict()
        parent[root] = None
        queue = deque()
        queue.append(root)

        #
        while not (p in parent and q in parent):
            node = queue.popleft()
            
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set()
        curr = p
        while curr:
            ancestors.add(curr)
            curr = parent[curr]
        # now we have all ancestors of p
        # so we can start looking for the overlap when iterating
        # upwards from q
        while q not in ancestors:
            q = parent[q]
        return q