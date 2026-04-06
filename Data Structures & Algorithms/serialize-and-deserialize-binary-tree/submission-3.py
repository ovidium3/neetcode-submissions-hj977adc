# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # can prob do this by getting inorder and preorder
    # array encoded to a str then just deserializing to that
    # essentially turning this to medium problem of creating
    # binary tree from pre + inorder traversals
    # NOPE! since we can have duplicate numbers this wont work
    # just do preorder + null nodes

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def recurse(root):
            if not root:
                preorder.append('N')
                return
            preorder.append(str(root.val))
            recurse(root.left)
            recurse(root.right)
        
        recurse(root)

        res = ",".join(preorder)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        if preorder == ['']:
            return None
        
        ctr = [0]

        def construct():
            i = ctr[0]
            # base case: null node, increment ct and continue
            if preorder[i] == 'N':
                ctr[0] += 1
                return
            
            root = TreeNode(preorder[i])
            ctr[0] += 1

            root.left = construct()
            root.right = construct()

            return root

        return construct()
