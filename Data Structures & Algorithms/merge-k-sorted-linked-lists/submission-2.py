# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force approach:
        # scan thru each linked list and just pick the 
        # one that is smallest value out of all possible
        # values to select from
        # we could try just merging two at a time
        # but that would be horribly inefficient
        # optimization: use a minHeap to push all node values

        k = len(lists)
        nodes = [0] * k
        for i in range(k):
            nodes[i] = lists[i]

        res = ListNode() # dummy node
        curr = res
        while True:
            currMinVal = float('inf')
            currMinIdx = None
            for i in range(k):
                node = nodes[i]
                if node and node.val < currMinVal:
                    currMinVal = node.val
                    currMinIdx = i
            
            # no more nodes left to process, return res
            if currMinIdx == None:
                return res.next
            
            # else we need to update the index at which we 
            # found that curr min node and add to our res
            currMinNode = nodes[currMinIdx]
            nodes[currMinIdx] = currMinNode.next
            currMinNode.next = None
            curr.next = currMinNode
            curr = curr.next
