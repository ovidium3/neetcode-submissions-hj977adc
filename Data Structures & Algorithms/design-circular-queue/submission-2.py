class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:
    # intuition: use linked list to not have constant
    # memory usage of the limit
    # rather it is dynamically sized each time you enqueue
    def __init__(self, k: int):
        # dummyL is front, dummyR is back
        self.dummyL = ListNode()
        self.dummyR = ListNode()
        self.dummyL.next = self.dummyR
        self.dummyR.prev = self.dummyL
        self.size = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        # enqueue on the right side
        if self.isFull():
            return False

        oldRear = self.dummyR.prev
        newNode = ListNode(value, oldRear, self.dummyR)
        self.dummyR.prev = newNode
        oldRear.next = newNode

        self.size += 1
        return True


    def deQueue(self) -> bool:
        # dequeue from the left side
        if self.isEmpty():
            return False

        oldFront = self.dummyL.next
        newFront = oldFront.next
        newFront.prev = self.dummyL
        self.dummyL.next = newFront
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummyL.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummyR.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()