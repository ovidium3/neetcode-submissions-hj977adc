from collections import defaultdict

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LFUCache:
    # define a series of helper functions to 
    # intiialzie dummy L and dummy R nodes for each
    # frequency
    def _init_list_nodes(self):
        L = ListNode()
        R = ListNode()
        L.next = R
        R.prev = L
        return (L, R)
    
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, freq, node):
        L, R = self.nodeLists[freq]
        tmp = L.next
        L.next = node
        node.prev = L
        node.next = tmp
        tmp.prev = node

    # intuition: organize by frequency a series of lists
    # so that we can always pop from the min freq list
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.freqs = {}  # key -> [freq, node]
        self.nodeLists = defaultdict(self._init_list_nodes)  # freq -> (L, R)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.freqs:
            return -1

        freq, node = self.freqs[key]

        # remove from old freq list
        self._remove(node)

        L, R = self.nodeLists[freq]
        if L.next == R:  # list empty
            if self.minFreq == freq:
                self.minFreq += 1

        # move to higher freq
        self.freqs[key][0] += 1
        self._insert(freq + 1, node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.freqs:
            # update value + reuse get to bump freq
            self.freqs[key][1].val = value
            self.get(key)
            return

        if self.size == self.cap:
            # evict LFU (LRU within that freq)
            L, R = self.nodeLists[self.minFreq]
            lru = R.prev

            self._remove(lru)
            del self.freqs[lru.key]
            self.size -= 1

        # insert new node with freq = 1
        newNode = ListNode(key, value)
        self.freqs[key] = [1, newNode]
        self._insert(1, newNode)

        self.minFreq = 1
        self.size += 1