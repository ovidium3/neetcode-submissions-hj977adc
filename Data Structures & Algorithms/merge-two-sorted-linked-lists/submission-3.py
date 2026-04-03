# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # most ppl like to setup a dummy node to avoid edge case of inserting into empty list
        tail = dummy # keep track of current tail, to append at

        while list1 and list2: # need both to compare, bc once one has no more elts, just append the other to the result
            if list1.val < list2.val: # update tail ptr to new "end" elt, and update list1 pointer to next
                tail.next = list1
                list1 = list1.next
            else: # case where list2 val is <=, need to link tail to list2 instead
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1: # case where one list has a few extra nodes left in it
            tail.next = list1
        elif list2: # only other possible case where other list has extra nodes. NEVER both.
            tail.next = list2
        
        return dummy.next # list starts after dummy ptr
