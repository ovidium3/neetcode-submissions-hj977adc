# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # base case of null node
        
        return self.helper(0, root)
        

    def helper(self, depth: int, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # base case of no extra node, so don't increment depth

        return 1 + max(self.helper(depth, root.left), self.helper(depth, root.right))