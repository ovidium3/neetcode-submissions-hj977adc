# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # intuition: we know that a path can span across 
        # any sequence of nodes as long as they are not
        # repeating, meaning it can either be the largest path
        # of any child nodes, OR it can include the root node itself
        # so we can do a DFS with classic base case of null = 0
        # and then just compute the left max and right max
        # but we zero them out in case a path is negative, indicatres we dont
        # use the path, and then update our res variable
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            # store result
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # negative res we dont want
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update res in case current path is longer
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # return val of curr path that CAN be extended up to parent!
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]