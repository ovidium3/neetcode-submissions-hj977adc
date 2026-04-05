class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    # slightly hacky design by reusing function
    # to delete node then reappend 
    # instead of just rearranging the pointers directly
    # still follows O(1) time operation tho
    def __init__(self, capacity: int):
        # intuition: linked list ordering of 
        # least recently used
        self.dummyL = ListNode()
        self.dummyR = ListNode()
        self.dummyL.next = self.dummyR
        self.dummyR.prev = self.dummyL
        self.cap = capacity
        self.size = 0
        self.mapping = defaultdict(ListNode) # key : Node

    def get(self, key: int) -> int:
        # this also needs to rearrange list
        # since it indicates we are accessing a val
        # therefore must rearrange
        if key not in self.mapping:
            return -1
        v = self.mapping[key].val
        self.put(key, v)

        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # remove the old node from the list as we will
            # append the new one to indicate freshness
            curr = self.mapping[key]
            prev = curr.prev
            nxt = curr.next

            # this is the one we want to delete
            nxt.prev = prev
            prev.next = nxt

            del self.mapping[key]
            self.size -= 1

        elif self.cap == self.size:
            # delete LRU and update ptrs
            # without having to remove from middle of list
            LRU_node = self.dummyL.next
            del_key = LRU_node.key
            nextLRU = LRU_node.next
            nextLRU.prev = self.dummyL
            self.dummyL.next = nextLRU
            del self.mapping[del_key]
            self.size -= 1
        
        # finally can insert new val to the right
        old_MRU = self.dummyR.prev
        newNode = ListNode(key, value, old_MRU, self.dummyR)
        old_MRU.next = newNode
        self.dummyR.prev = newNode

        self.mapping[key] = newNode
        self.size += 1
