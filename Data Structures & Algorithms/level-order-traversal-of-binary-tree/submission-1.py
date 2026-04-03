# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        
        q.append(root) # init queue with root node, don't even need level

        while q:
            subLvl = [] # init sublist for current level

            for i in range(len(q)): # this is how you iterate over the current queue inputs only
                curr = q.popleft() # how to extract from queue - pop from left

                if curr: # ignore null values that were added to the queue
                    subLvl.append(curr.val) # add to result sublevel
                    q.append(curr.left)
                    q.append(curr.right)

            if subLvl:
                res.append(subLvl)

        return res