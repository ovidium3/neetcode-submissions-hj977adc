# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next # assign two pointers, slow and fast, to check through for dupes
        # if the fast surpasses the slow there is a cycle, else it reaches the end and there's no cycle
        while fast and fast.next:
            if slow == fast: # case where fast loops around and catches up to slow indicating a cycle
                return True
            
            # update loop condition
            slow = slow.next
            fast = fast.next.next

        return False