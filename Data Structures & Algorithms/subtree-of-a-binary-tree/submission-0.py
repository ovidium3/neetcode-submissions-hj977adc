# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not subRoot: # no more subroot nodes to comp so it must be
            return True
        if not root: # no root to compare to means there's no way it can be a subtree
            return False
        
        # equality check - see if subroot is same as current "root" youre checking from
        if self.isSameTree(root, subRoot):
            return True

        # default case - check if either of root's children contain subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # helper function - lc 100
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # this function does not need modification since a subtree can only be valid if
        # it is EXACTLY like ALL descendants, not just exists within a segment of the initial tree
        # base cases
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False # rest of cases like if only one node exists or values don't match