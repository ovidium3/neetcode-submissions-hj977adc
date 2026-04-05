# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            final = None
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    final = curr.val
            if final:
                res.append(final)
        
        return res
