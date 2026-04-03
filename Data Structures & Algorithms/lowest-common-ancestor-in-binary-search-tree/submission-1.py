# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base cases - if root node is equal to p or q, then that is automatically the LCA
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        # now check which subtree to keep looking in, if any
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root # must be in separate subtrees so this current node is the LCA