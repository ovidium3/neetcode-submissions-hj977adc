# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # init list of lists

        queue = deque() # set up queue and add in root node to start
        queue.append(root)

        while queue: # iterate thru one level at a time
            level = [] # set up list for current level

            for i in range(len(queue)): # go thru entire level (current queue)
                node = queue.popleft()
                if node: # filter only children that were added that DO exist
                    level.append(node.val) # add nodes that exist to the current list
                    queue.append(node.left) # will be checked for null later
                    queue.append(node.right) # also will be checked later

            if level: # only add in non-empty level lists to result
                res.append(level)

        return res