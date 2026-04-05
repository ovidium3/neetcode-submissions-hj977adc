# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # intuition: we want to recursively find inorder
        # successor, i.e. leftmost val in right subtree
        # to replace with if both children exist
        # we dont care about balancing like an AVL tree or
        # red/black subtree
        if not root:
            return None # nothing to delete here
        
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # else two children, find inorder successor
            # i.e. leftmost val in right subtree
            # as that would be a valid replacement
            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
       
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
        