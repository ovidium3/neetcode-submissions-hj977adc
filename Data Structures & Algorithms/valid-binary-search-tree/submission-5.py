# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # intuition: only invariant is that we must ensure that
        # the current left val if it exists is smaller than the current
        # right val if it exists, as well as the subchildren both being BSTs
        # ISSUE: need to consider bounds since ALL elements
        # of the left / right subtree must fit within bounds
        # which translates literally into code
        # as the last line is returning if both subchildren are valid or not
        
        def checkBST(root, lo, hi):        
            if not root:
                return True # base case: null is valid BST
            
            # root falls out of bounds
            if root.val <= lo or root.val >= hi:
                return False

            # case where left child val is geq root val
            # OR right child val is leq root val
            if root.left and root.val <= root.left.val:
                return False
            if root.right and root.val >= root.right.val:
                return False
            
            return checkBST(root.left, lo, root.val) and checkBST(root.right, root.val, hi)
        
        return checkBST(root, float('-infinity'), float('inf'))