# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec: # can also do DFS via preorder traversal
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        # need to setup a BFS, using a queue, to create an inorder traversal
        res = [] # can also use a list and join at the end with "," delimeter

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)): # go through one "level" at a time (BFS)
                curr = q.popleft()

                if curr:
                    res.append(str(curr.val))

                    # add child nodes to queue, regardless if null - may create edge case of all null nodes
                    q.append(curr.left)
                    q.append(curr.right)
                else: # can't just leave this blank - have to encode null node
                    res.append('n')

        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if data == "n": # edge case of null tree
            return None

        # need to unpack inorder traversal
        
        nodeVals = data.split(',') # creates list instantly from comma separated values
        root = TreeNode(int(nodeVals[0]))

        q = deque()
        q.append(root)

        i = 1 # start accessing node values list from i = 1 since [0] is root
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

    # ALT SOLUTION: DFS
    # essentially the same thing but using recursion instead of a queue
    # global var in decode to point to index of list to get node val. 2 null nodes == end of node lineage
    # Encodes a tree to a single string.
    '''
    def serialize(self, root: TreeNode) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
    '''