# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case - no values left to reorder
        if not preorder or not inorder:
            return None

        first = preorder[0] # current node's "value"

        root = TreeNode(first)
        inorderIdx = inorder.index(first) # middle value that splits apart the subtrees in the INorder

        # extract new preorders for recursive calls
        leftPre = preorder[1 : inorderIdx + 1] # +1 to skip over inorderIdx?
        rightPre = preorder[inorderIdx + 1 : ] # start past inorder index and go to end

        # extract new inorders for recursive calls
        leftIn = inorder[ : inorderIdx] # go up to inorder index, not including
        rightIn = inorder[inorderIdx + 1 : ] # identical to right preorder

        # arrange l and r ptrs with recursive calls
        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)

        return root # after tree is finally done being built, return root node after recursing back up