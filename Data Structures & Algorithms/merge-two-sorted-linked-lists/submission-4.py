# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, one for each node.
        # increment the smaller node val pointer, ties broken arbitrarily?
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        curr1 = list1
        curr2 = list2

        head = result = None
        if curr1.val < curr2.val:
            head = result = curr1
            curr1 = curr1.next
        else: # curr2.val <= curr1.val
            head = result = curr2
            curr2 = curr2.next

        while curr1 and curr2:  # need both to have vals to check
            if curr1.val > curr2.val:
                temp = curr2
                result.next = temp
                curr2 = curr2.next
            else: # curr2.val >= curr1.val, break ties arbitrarily
                temp = curr1
                result.next = temp
                curr1 = curr1.next
            result = result.next
        
        # at this point, one or both of these will be None
        if curr1 != None:
            result.next = curr1
        elif curr2 != None:
            result.next = curr2

        return head
