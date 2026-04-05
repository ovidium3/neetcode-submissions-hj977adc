# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # intuition: we can clearly see that if any single
        # max depth branch is > 1 length compared to shortest,
        # then we return False
        # balance means that each subtree is of height diff <= 1
        # so we must check every node
        # not simply a max depth v min depth, we check for each node
        # must compute height and balance simultaneously, to avoid re checking!
        def dfs(root):
            if not root:
                return [True, 0]
            leftBalanced, leftH = dfs(root.left)
            rightBalanced, rightH = dfs(root.right)
            balanced = leftBalanced and rightBalanced and abs(leftH - rightH) <= 1
            return [balanced, 1 + max(leftH, rightH)]

        return dfs(root)[0]