# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # just do an inorder traversal, put each elt in an array, find kth value
        ct, res = 0, 0 # declare count and result outside of inorder recursive func

        def inorder(root: Optional[TreeNode]):
            nonlocal ct, res # mark vars as nonlocal to change outside of func
            # base case of null root 
            if not root:
                return
            
            # inorder traversal: check left child, then value, then right child
            inorder(root.left)
            ct += 1 # increment counter
            if ct == k:
                res = root.val
                return# root.val
            inorder(root.right)
        
        inorder(root) # call func to populate array
        return res

        # iterative solution with stack
        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur: # go left until null
                stack.append(cur) # add to stack to check later
                cur = cur.left
            
            cur = stack.pop() # start processing from stack
            n += 1
            if n == k:
                return cur.val # we have reached kth value, so return it
            cur = cur.right # else we keep checking to the right