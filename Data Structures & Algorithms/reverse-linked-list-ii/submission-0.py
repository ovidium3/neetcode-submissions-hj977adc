# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # intuition: dummy node next value always
        # points at the new head of the list
        # if we end up reversing starting at the original
        # head of the list
        # 3 phases: 
        # 1. reach left node
        # 2. execute reversal for r - l + 1 iterations
        # 3. clean up ptrs and make final links
        dummy = ListNode(0, head) # next points to original head
        leftPrev = dummy
        curr = head # or dummy.next, same thing
        for _ in range(left - 1): # since we 1 index with a dummy node
            leftPrev = curr
            curr = curr.next

        # phase two: reverse from L to R
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # phase three: set next after left Prev (L)
        # to point to the remainder of list
        # and then set leftPrev's next to the prev
        # which is the start of the reversed portion
        leftPrev.next.next = curr # leftPrev.next == L
        leftPrev.next = prev # prev == R

        return dummy.next # new head if we ended up reassigning