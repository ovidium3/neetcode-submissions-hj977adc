# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return # base case of null node, end recursive cycle

        root.left, root.right = root.right, root.left # need to assign BOTH at once to avoid overwriting only one
        
        # recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root # final result