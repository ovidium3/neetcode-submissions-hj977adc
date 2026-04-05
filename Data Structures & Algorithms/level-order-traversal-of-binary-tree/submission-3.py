# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # intuition: create a list for each sublevel
        # that we find, i.e. a BFS using queue
        # and build up a list for each level in the queue
        # then append it to the res at the end if the nodes 
        # have values in them
        res = []

        q = deque()
        
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                res.append(level)

        return res