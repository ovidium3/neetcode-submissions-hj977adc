# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # O(n) time since dfs
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs like usual with tree problems
        res = [root.val] # make global a list so it is easier to modify inside recursive func
        
        def dfs(root: Optional[TreeNode]) -> int:
            # base case
            if not root:
                return 0

            # do recursive calls now, handle them later
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # edge case - path sums are less than 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            # max sum WITHOUT split
            return root.val + max(leftMax, rightMax) # can't choose both, because then we'd be splitting
        
        dfs(root)
        return res[0]