# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: # base case, null tree is balanced
            return True

        # local func to get height, based off lc easy
        def getHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        maxL, maxR = getHeight(root.left), getHeight(root.right)
    
        if abs(maxL - maxR) > 1: # if heights differ by more than 1, it is not balanced
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right) # else recursively keep checking