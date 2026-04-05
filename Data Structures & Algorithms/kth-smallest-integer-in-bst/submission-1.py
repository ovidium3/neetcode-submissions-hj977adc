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

        res = []

        def collectVals(root):
            if not root:
                return
            
            res.append(root.val)
            collectVals(root.left)
            collectVals(root.right)
        
        collectVals(root)
        res.sort()
        return res[k - 1]
