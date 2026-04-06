# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # issue: multiple nodes may have value
        # but we can only delete leaf nodes
        # thing is, we can create new leaf nodes that 
        # were previously unaccessible for deletion
        # NOTE: not a BST, must brute force this
        # use post order since we want to check leaf nodes
        # BEFORE checking curr node!
        if not root:
            return None

        # update left and right children
        # BEFORE processing current node
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # return nothing if we want to indicate deleting the node
        if root.val == target and not root.left and not root.right:
            return None

        return root