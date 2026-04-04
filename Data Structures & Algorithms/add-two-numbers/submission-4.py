# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        if carry:
            newNode = ListNode(1)
            node.next = newNode

        return res.next