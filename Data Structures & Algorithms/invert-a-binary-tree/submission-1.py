# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None # base case of null node, end recursive cycle. can just return nothing as well

        root.left, root.right = root.right, root.left # need to assign BOTH at once to avoid overwriting only one
        # can also create a temp node and swap one at a time but this one liner works too
        
        # recursive calls - pre or post order, doesnt matter. DFS
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root # final result