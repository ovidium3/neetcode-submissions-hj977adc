# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # same as inorder, but this time we want to just check
        # the val before going left, then right
        res = []

        def traversePreorder(root):
            if not root:
                return # base case null
            
            res.append(root.val)
            traversePreorder(root.left)
            traversePreorder(root.right)

        traversePreorder(root)
        return res