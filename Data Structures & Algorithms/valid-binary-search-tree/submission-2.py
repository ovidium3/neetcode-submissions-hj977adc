# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root: Optional[TreeNode], lessVal: int, greaterVal: int) -> bool:
            # base cases
            if not root: # nothing to check here, is valid by default
                return True
            if (root.left and root.left.val >= root.val) or (root.left and root.left.val <= lessVal): # left child must be <
                return False
            if (root.right and root.right.val <= root.val) or (root.right and root.right.val >= greaterVal): # right child must be >
                return False

            # children either don't exist or are valid so keep checking
            return validate(root.left, lessVal, root.val) and validate(root.right, root.val, greaterVal)

        return validate(root, float('-inf'), float('inf'))