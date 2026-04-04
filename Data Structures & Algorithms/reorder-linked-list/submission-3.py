# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        nodePtrs = []

        curr = head
        while curr:
            nodePtrs.append(curr)
            curr = curr.next
        
        # approach: set up two pointers
        # s.t. next left node ptr points
        # to the node in the right part,
        # and then the next right ptr
        # points to the left node.
        # break condition if l == r
        l, r = 0, len(nodePtrs) - 1
        
        while l < r:
            nodePtrs[l].next = nodePtrs[r]
            l += 1
            if l == r:
                break
            nodePtrs[r].next = nodePtrs[l]
            r -= 1
        
        nodePtrs[l].next = None
