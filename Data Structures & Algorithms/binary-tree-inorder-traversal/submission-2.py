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
        # O(n) time and recursion stack space, as well as output space
        # can do it in O(1) space but since already producing O(n) output
        # might as well do this. O(1) space means just iteratively checking nodes
        res = []

        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        traverse(root)
        return res