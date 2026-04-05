# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # intuition: we can just go check each node in the tree
        # and compare to see if first of all both nodes are null,
        # that is a match
        # if one exists and the other doesnt, then that is False
        # if the values are different, not a match
        # else keep checking left and right children
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if not p and q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)