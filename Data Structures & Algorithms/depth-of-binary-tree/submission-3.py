# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # intuition: we can just do bfs down 
        # taking the maximum length of each path as
        # we go down adding 1 to current path length
        if not root:
            return 0 # base case height of 0 at root
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
