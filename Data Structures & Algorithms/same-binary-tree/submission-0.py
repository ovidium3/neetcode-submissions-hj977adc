# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # base case 1: neither node exists, so it is the same
            return True
        if (not p and q) or (p and not q): # if only one node exists, they can't possibly be equal
            return False
        if p.val != q.val: # both nodes exist, so compare values
            return False
        
        # keep comparing remaining trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)