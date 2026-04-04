# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        curr = head
        sz = 0
        while curr:
            sz += 1
            curr = curr.next

        remove_idx = sz - n
        # special case: if we pop head
        # then just set head to be next
        if remove_idx == 0:
            return head.next

        idx = 0
        curr = head
        while curr:
            if idx == remove_idx - 1:
                # we stop BEFORE the node to delete
                # and just override the link
                curr.next = curr.next.next
                return head
            idx += 1
            curr = curr.next

        return head