# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # intuition: it is a subroot if and only if
        # the subroot exists in the tree AND it has no
        # extra descendants lingering below
        # this is a brute force way to solve it
        # optimization: serialize using string? how the hell do
        # you come up with that ? 

        def checkSubTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if root and not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return checkSubTree(root.left, subRoot.left) and checkSubTree(root.right, subRoot.right)
        
        if not root:
            return False

        if checkSubTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        