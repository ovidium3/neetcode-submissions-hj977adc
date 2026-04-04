# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # intuition: we want to go thru the list and track 
        # the prev element
        # first we make a copy of the node, i.e.
        # the next node, and then we overwrite the next
        # node to be the prev node. then we update the
        # prev ptr to track the current node
        # and then lastly update the condition of the loop
        # to point to the saved real next tmp value
        if not head:
            return None
        
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev