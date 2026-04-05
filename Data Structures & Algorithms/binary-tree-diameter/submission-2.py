# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # intuition: we can either take the height of the tree directly,
        # or the current node (1) + the left and right subtree heights
        if not root:
            return 0
        
        res = [0] # can access list, but not int inside helper
        
        def dfs(root):
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]