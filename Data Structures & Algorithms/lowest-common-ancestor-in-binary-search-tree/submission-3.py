# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # intuition: use the fact that this is a BST (smaller val L)
        # and try to find the value of p and q accordingly
        # i.e. if we are looking at a given node,
        # and see that the value is larger than p and smaller than q
        # or something like that, then we know it must be the ancestor
        if not root:
            return None
        
        # curr val is larger than BOTH: try to find LCA
        # in the left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # found target
            return root