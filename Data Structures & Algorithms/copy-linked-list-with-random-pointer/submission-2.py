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
        # two pass hash solution: first build up a map
        # of the nodes, then go ahead and fill in
        # all the pointers using the map
        # optimization: we can just directly compute in a single
        # pass by creating the node on access in hashmap
        oldToNew = defaultdict(lambda: Node(0)) # maps old nodes to new nodes
        oldToNew[None] = None

        curr = head
        while curr:
            # update new node val
            oldToNew[curr].val = curr.val

            # update new node's next val
            oldToNew[curr].next = oldToNew[curr.next]

            # update new node's random val
            oldToNew[curr].random = oldToNew[curr.random]

            # regular iteration to continue loop
            curr = curr.next
        
        return oldToNew[head]