# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # intuition: inorder traversal means visit left down as far as yu can
        # before getting middle val, then traverse entire right side
        # down as far as you can. every time you go left first
        # THEN check val, then continue down right
        res = []

        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        traverse(root)
        return res