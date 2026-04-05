# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # intuition: we can just go down the binary
        # tree but we have to track the current
        # maximum value in the path
        # if value >= then node is good
        # fix count off by one err init res to 0
        # instead of 1 since the condition
        # is >= instead of just >
        if not root:
            return 0 #base case; no node to consider

        res = [0]

        def findNodes(root, maxVal):
            if not root:
                return
            
            if root.val >= maxVal:
                res[0] += 1
                maxVal = root.val
            findNodes(root.left, maxVal)
            findNodes(root.right, maxVal)
            
        findNodes(root, root.val)

        return res[0]