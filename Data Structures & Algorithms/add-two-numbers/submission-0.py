# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = False
        
        while l1 or l2 or carry:
            # calculate current sum and handle potential carry value
            currSum = 1 if carry else 0
            if l1:
                currSum += l1.val
            if l2:
                currSum += l2.val

            # update carry for next time    
            if currSum > 9:
                currSum -= 10
                carry = True
            else:
                carry = False

            curr.next = ListNode(currSum) # insert new node with current value

            # update while loop conditions
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        return dummy.next # start of the new linked list containing the result