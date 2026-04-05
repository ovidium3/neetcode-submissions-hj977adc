# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # same as preorder and inorder idea, but this time
        # we want to append val only after checking right side
        res = []

        def traversePostorder(root):
            if not root:
                return
            
            traversePostorder(root.left)
            traversePostorder(root.right)
            res.append(root.val)
        
        traversePostorder(root)
        return res