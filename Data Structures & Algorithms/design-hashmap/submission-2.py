class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:

    def __init__(self):
        # init with dummy node
        self.buckets = [ListNode(-1, -1) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        moddedKey = key % 1000
        node = self.buckets[moddedKey]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        moddedKey = key % 1000
        node = self.buckets[moddedKey]
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1 # should be -1 if we cycle to end of list and no match

    def remove(self, key: int) -> None:
        moddedKey = key % 1000
        node = self.buckets[moddedKey]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# basic solution:
# class MyHashMap:

#     def __init__(self):
#         self.mapping = [-1] * 1000001

#     def put(self, key: int, value: int) -> None:
#         self.mapping[key] = value

#     def get(self, key: int) -> int:
#         return self.mapping[key]

#     def remove(self, key: int) -> None:
#         self.mapping[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)