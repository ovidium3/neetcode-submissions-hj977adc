# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # intuition: go ahead and count the number of nodes
        # and then determine how many reversals we have to make
        # if k == 1, does that mean we just return initial list?
        # this is an O(n) soution really more like 2* n worst case
        if k == 1:
            return head
        
        dummy = ListNode(0, head) # since we are basically guaranteed
        # that we are gonna be rearranging the head
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break # cannot rearrange a full next k elts
            # might need to do two loops in here
            # so that first loop reverses
            # and second loop fixes start / end ptrs?
            # or just do it all in one go
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next

            # for i in range(k)
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # fix up ptrs: set the previous next to kth,
            # and the previous to prev next (after updating)
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr