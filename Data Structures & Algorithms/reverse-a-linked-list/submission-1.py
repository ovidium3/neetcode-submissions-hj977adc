# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # need to track current AND previous nodes to relink properly

        while curr: # keep looping thru until no more nodes left
            temp = curr.next # create temp node referring to future node
            curr.next = prev # override connection to next node to point to prev node
            prev = curr # update prev node to current node
            curr = temp # update current node to the initial next node in line - saved in temp node
            
        return prev # since prev will be updated to be the current node, as current node will point to nullptr