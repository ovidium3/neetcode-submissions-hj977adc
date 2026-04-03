# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        # need to setup a BFS, using a queue, to create an inorder traversal
        res = ""

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)): # go through one "level" at a time (BFS)
                curr = q.popleft()

                if curr:
                    res += "," # used to know where to start/stop decoding str
                    res += str(curr.val)

                    # add child nodes to queue, regardless if null - may create edge case of all null nodes
                    q.append(curr.left)
                    q.append(curr.right)
                else: # can't just leave this blank - have to encode null node
                    res += ",n"

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if data == ",n": # edge case of null tree
            return None

        # need to unpack inorder traversal
        
        nodeVals = data.split(',') # creates list [1-indexed] since first , has nothing preceding it
        root = TreeNode(int(nodeVals[1]))

        q = deque()
        q.append(root)

        i = 2 # start accessing node values list from i = 2 since [0] is empty, [1] is root
        while q:
            curr = q.popleft()

            # left child
            if nodeVals[i] != "n":
                leftChild = TreeNode(int(nodeVals[i])) # type conversion since node vals are ints
                curr.left = leftChild
                q.append(leftChild)
            
            i += 1 # update idx for right child

            # right child
            if nodeVals[i] != "n":
                rightChild = TreeNode(int(nodeVals[i])) # type conversion since node vals are ints
                curr.right = rightChild # update right child ptr
                q.append(rightChild) # add child to queue to process its children and so forth
            
            i += 1 # update idx again for next left child
        
        return root