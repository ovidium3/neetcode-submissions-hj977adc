# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(n) time, O(1) space. alt solution: O(n) space by using an array
    def reorderList(self, head: Optional[ListNode]) -> None:
        # subproblem 1: find midpoint of the list
        slow, fast = head, head.next # init slow ptr (+1), fast ptr (+2) at nodes 1, 2 respectively
        while fast and fast.next: # keep going until fast reaches end; therefore slow reached midpt
            slow = slow.next
            fast = fast.next.next

        midPtr = slow
        secondStart = midPtr.next # new node to keep track of start of second half list
        midPtr.next = None # handle edge case where "new" last node points to start of second half

        # subproblem 2: reverse second half of list
        prev, curr = None, secondStart
        while curr:
            temp = curr.next # create temp ptr to next node
            curr.next = prev # override next node as prev node
            prev = curr # update prev node to be curr one
            curr = temp # update curr node to be old/saved next node
        
        # subproblem 3: splice both lists together
        list1, list2 = head, prev
        while list2: # keep adding nodes from second list. keep track of l2 since that is shorter
            temp1 = list1.next # save new list1 value to update later
            temp2 = list2.next # save new list2 value to update later
            
            list1.next = list2 # update next node to be from list2
            list1.next.next = temp1 # make sure list2 next node points back to list1 saved next node

            list1 = temp1 # update for while to work properly
            list2 = temp2 # update for while loop condition
