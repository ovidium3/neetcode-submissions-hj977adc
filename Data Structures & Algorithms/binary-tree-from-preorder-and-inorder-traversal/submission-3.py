# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # intuition: we know first element of preorder is always teh root
        # so from there can just split the inorder array into two halves
        # recursively to build left and right subtrees
        # OPTIMIZATION: use hash map to enumerate inorder indices
        # and avoid n^2 runtime due to index slicing
        # map value -> index in inorder for O(1) lookup
        idx_map = {v: i for i, v in enumerate(inorder)}
        
        self.pre_idx = 0  # pointer into preorder
        
        def dfs(left, right):
            # bounds represent current inorder subtree
            if left > right:
                return None
            
            # current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # split point in inorder
            mid = idx_map[root_val]
            
            # build left subtree first (important: preorder order)
            root.left = dfs(left, mid - 1)
            
            # then right subtree
            root.right = dfs(mid + 1, right)
            
            return root
        
        return dfs(0, len(inorder) - 1)
        
        # if not preorder or not inorder:
        #     return None # no more elts to deal with, base case
        
        # root = TreeNode(preorder[0]) # first elt of preorder is always root

        # mid = inorder.index(preorder[0]) # find idx in inorder: unique vals guaranteed!
        # # build left subtree:
        # # preorder[1:mid+1] == skip root, take next `mid` nodes
        # # inorder[:mid] == left subtree portion
        # root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # # build right subtree:
        # # preorder[mid+1:] == remaining nodes after left subtree
        # # inorder[mid+1:] == right subtree portion
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # return root # simple, once done recursing