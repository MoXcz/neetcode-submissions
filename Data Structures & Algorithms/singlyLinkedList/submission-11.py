class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next

        return curr.val if curr else -1
        

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val, self.head.next)
        self.head.next = newHead

        if not newHead.next:
            self.tail = newHead
        
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head

        for i in range(index):
            if curr is None:
                return False
            
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr