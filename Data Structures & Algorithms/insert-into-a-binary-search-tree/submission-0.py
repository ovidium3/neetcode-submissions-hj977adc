# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # intuition: we can traverse the tree until we 
        # find that either there is no root left (in which case)
        # we can insert the element, or we just go down l / r
        # path until we find a position
        # base case is to just return the node that we 
        # will insert because if we have traversed the entire
        # path and validated it, we know we can insert there
        # and it is the first possible valid point
        # as any valid insert point gets accepted?
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else: # val > root.val
            root.right = self.insertIntoBST(root.right, val)
        
        return root # once we done recursing