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
        

        pRight, qRight = False, False

        # compare values since it is a BST to see which direction to go in
        if p.val > root.val:
            pRight = True
        if q.val > root.val:
            qRight = True
        
        if pRight == qRight:
            if pRight:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)
            
        # else they are in diff subtrees so this current node is the LCA
        return root
            
        