"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None} # maps old nodes to new nodes
        
        curr = head
        while curr:
            newCurr = Node(curr.val)
            oldToNew[curr] = newCurr
            curr = curr.next
        curr = head
        while curr:
            newCurr = oldToNew[curr]
            newCurr.next = oldToNew[curr.next]
            newCurr.random = oldToNew[curr.random]
            curr = curr.next
        
        return oldToNew[head]