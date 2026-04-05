# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force: collect ALL values in the tree
        # then check an auxiliary array to find
        # the kth smallest value? O(n) time and space
        # optimal: do inorder traversal which guarantees
        # that k-th visited element is gonna be the k-th smallest
        res = [0]
        iterations = [0]

        def inorderTraverse(root):
            if not root:
                return

            inorderTraverse(root.left)
            iterations[0] += 1
            if iterations[0] == k:
                res[0] = root.val
                return
            inorderTraverse(root.right)
        
        inorderTraverse(root)
        return res[0]
