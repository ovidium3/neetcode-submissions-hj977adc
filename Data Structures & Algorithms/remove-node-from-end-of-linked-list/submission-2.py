# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(n)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set up two pointers, n distance apart so that once right reaches end of list,
        # left will be pointing at exactly n nodes from the end
        dummy = ListNode(0, head) # val doesnt matter, but needs to point to head

        left, right = dummy, head
        currDist = 0

        while currDist < n:
            right = right.next
            currDist += 1

        while right:
            left = left.next
            right = right.next

        prev, curr = left, left.next
        prev.next = curr.next

        return dummy.next

        '''


        midCt = 1
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            midCt += 1

        sz = 1 + (midCt * 2) # default case, list is an odd num of nodes
        if fast: # case where list is an even num of nodes
            sz -= 1 # need to adjust list sz by sub one, since there isnt an extra odd node at the end
        
        toRemove = sz - n # total num of nodes to remove from the START

        # iterate from the start to find node to remove
        prev, curr = None, head
        ct = 0
        while curr:
            if ct == toRemove:
                prev.next = curr.next
                del curr
                return head
            ct += 1
            prev = curr
            curr = curr.next
        '''