# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make connections before breaking them        
        # create dummy node
        # point dummy node to curr next node
        # point curr next node to the prev node
        # update curr node to be the temp next (old curr next)
        # sever link between current node and next
        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev # since curr points past end