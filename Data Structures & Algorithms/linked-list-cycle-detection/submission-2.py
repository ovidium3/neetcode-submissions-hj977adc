# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if slow.next == None or fast.next == None or fast.next.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True