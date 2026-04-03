# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # need a pointer to the node before the next group of k nodes that got reversed
        
        currNode = dummy # start at head to loop thru list once
        counter = 0

        while currNode: # loop through entire list once, finding k nodes to reverse at a time
            if counter != k: # increment currNode until we reach k nodes
                counter += 1
                currNode = currNode.next
                continue

            kth = currNode

            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # not sure wht these 3 lines do
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

            # update condition
            counter = 0
            currNode = temp

        return dummy.next