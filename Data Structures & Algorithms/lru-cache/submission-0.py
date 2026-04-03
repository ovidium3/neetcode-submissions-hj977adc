class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key to node containing k, v, and ptrs to prev and next
        
        # init two dummy nodes to keep track of LRU and most recent. left = LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # start helper funcs - remove and insert
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next # get nodes before and after node to remove
        prev.next, nxt.prev = nxt, prev # relink so that nodes before and after now point to each other

    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right # get node before most recently used and nullptr after
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # end helper funcs

    def get(self, key: int) -> int:
        if key in self.cache:
            # first update LRU by removing and re-inserting key to indicate it's most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # access val since we're using a mapping to a node
        return -1 # else key not in cache, simply return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        # have to check capacity to see if we have to evict LRU
        if len(self.cache) > self.capacity:
            # remove LRU from list AND delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]