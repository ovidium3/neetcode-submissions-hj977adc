# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # O(n * log(k)) where n = list length, k = num of lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # essentially doing merge sort on linked lists
        if not lists or len(lists) == 0:
            return None # edge case where we have a list of empty lists or an empty list

        # outer loop - O(log(k))
        while len(lists) > 1:
            mergedList = []

            # inner loop - O(n)
            for i in range(0, len(lists), 2): # increment by two since we are merging 2 lists at a time
                # have to check for odd num of lists just in case a second doesnt exist
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # can still merge with a null list
                mergedList.append(self.merge2Lists(l1, l2)) # merge two lists together at a time
            lists = mergedList # update lists with new merged result each iteration
        
        return lists[0] # return head of newly merged list

    # helper function to sort 2 linked lists - copy paste from lc easy
    def merge2Lists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode() # create dummy node, and tail to append to from each list
        tail = dummy

        while l1 and l2: # keep going thru both lists to comp values
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1: # once there is only one list left or possibly 0, check if any leftover vals to add
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next # return new "head"