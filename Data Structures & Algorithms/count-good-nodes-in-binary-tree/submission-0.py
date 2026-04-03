# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maxVal: int) -> int:
            if not root: # base case: no node
                return 0
            
            if root.val >= maxVal: # based on running highest val, count node as good or not by adding 1
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val) # good since val > max
            return dfs(root.left, maxVal) + dfs(root.right, maxVal) # not good since val < max
        
        return dfs(root, root.val) # call dfs func