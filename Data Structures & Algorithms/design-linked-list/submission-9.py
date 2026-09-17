class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        i = 0
        while curr and i <= index:
            if i == index:
                return curr.val

            curr = curr.next
            i+=1
        
        return -1


    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val, self.head.next)
        self.head.next = newHead

        if self.head == self.tail:
            self.tail = self.head.next
            

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        i = 0
        while curr and i <= index:
            if i == index:
                curr.next = ListNode(val, curr.next)
                if curr.next.next is None:
                    self.tail = curr.next
                return
        
            curr = curr.next
            i+=1
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head

        i = 0
        while curr and i <= index:
            if i == index and curr.next:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                return
        
            curr = curr.next
            i+=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)