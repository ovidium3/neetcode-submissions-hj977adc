# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at each node, run a height calculation from said node. res = max of those
        if not root:
            return 0

        self.currMax = 0 # need to make it a local var inside solution class to access inside nested func
        
        def heightDFS(root: Optional[TreeNode]) -> int: # NOT a self func, just a local nested func
            if not root: # base case
                return 0
            
            # compare heights of left and right child nodes to curent maximum diameter
            self.currMax = max(self.currMax, heightDFS(root.left) + heightDFS(root.right))
            
            # each recursive call increments diameter by 1
            return 1 + max(heightDFS(root.left), heightDFS(root.right))
            
        heightDFS(root) # actually call nested func to let it run
        return self.currMax