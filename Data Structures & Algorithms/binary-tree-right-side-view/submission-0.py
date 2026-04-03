# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # init res, and queue with root node
        res = []
        q = deque()
        q.append(root)

        while q: # conduct bfs, performing level order traversal
            val = float('inf') # set val to an arbitrary value out of range
            for i in range(len(q)): # check each node in queue, from left to right, updating val as we go
                curr = q.popleft()
                if curr: # only update val for nodes that are valid, as well as adding next lvl nodes to q
                    val = curr.val
                    q.append(curr.left)
                    q.append(curr.right)

            if val != float('inf'): # add val to result only if it is valid
                res.append(val)
        
        return res