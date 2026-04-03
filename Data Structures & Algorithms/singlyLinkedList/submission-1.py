# add in list node if not already there
class ListNode:
    def __init__(self, val: int, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = ListNode(-1)    # dummy node that gets ignored
    
    def get(self, index: int) -> int:
        curr = self.head.next
        currNum = 0
        while curr:
            if currNum == index:
                return curr.val

            curr = curr.next
            currNum += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        temp = ListNode(val, self.head.next)
        self.head.next = temp
        if not temp.next:
            # if list empty before inserting, head = tail = temp
            self.tail = temp

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        currNum = 0
        prev = self.head

        while currNum != index and prev:    # find node before target node
            prev = prev.next
            currNum += 1

        if prev and prev.next:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next

        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        return vals