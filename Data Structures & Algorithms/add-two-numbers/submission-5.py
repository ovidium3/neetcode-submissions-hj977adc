# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # intuition: we can just go thru and create two separate
        # arrays for each of the numbers in teh list nodes
        # and process them that way, performing basic addition
        # with a carry value that is either 0 or 1, ehnce we use a bool
        # if one list is longer than the other, we just append remaining 
        # elements by creating a new node each time
        # OPTIMIZATION: get rid of auxiliary lists and jsut perform computation
        # directly on the initial linked list itself
        # but since space is O(n) due to output list, 
        # might as well use the space here to make it like O(3n)
        num1 = []
        num2 = []
        curr = l1
        while curr:
            num1.append(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            num2.append(curr.val)
            curr = curr.next

        res = ListNode() # dummy node
        node = res
        carry = False
        for i in range(min(len(num1), len(num2))): # assume l1 nd l2 not always equal
            tmp = num1[i] + num2[i]
            if carry:
                tmp += 1
            
            newNode = ListNode()
            if tmp > 9:
                carry = True
            else:
                carry = False
            # in case it over 9. no harm if under 9
            newNode.val = tmp % 10

            node.next = newNode
            node = node.next

        start, end = len(num1), len(num2)
        if len(num1) > len(num2):
            start = len(num2)
            end = len(num1)
        
        for i in range(start, end):
            tmp = num1[i] if len(num1) > len(num2) else num2[i]
            if carry:
                tmp += 1
            newNode = ListNode()
            if tmp > 9:
                carry = True
            else:
                carry = False
            newNode.val = tmp % 10
            node.next = newNode
            node = node.next

        # dont forget we have to consider last carry value here
        # in the case where we need to append that last 1
        if carry:
            newNode = ListNode(1)
            node.next = newNode

        return res.next