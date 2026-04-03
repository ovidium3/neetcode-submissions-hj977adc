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
        # create a hashmap for each old random node to a copy
        oldToCopy = { None: None } # edge case where calling null value, need to return null

        # first pass - populate hashmap with a copy of each node
        curr = head
        while curr:
            copy = Node(curr.val) # just value
            oldToCopy[curr] = copy
            curr = curr.next
        
        # second pass - link pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            # set pointers
            copy.next = oldToCopy[curr.next] # extract new next from what the old next maps to
            copy.random = oldToCopy[curr.random] # extract new random from what old random maps to
            curr = curr.next

        return oldToCopy[head] # return the new head, which the old head maps to