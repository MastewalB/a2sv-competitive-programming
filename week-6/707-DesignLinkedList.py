class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while i < index:
            if not node:
                return -1
            node = node.next
            i += 1
        return node.val if node else -1 

    def addAtHead(self, val: int) -> None:
        if self.head:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        else:
            self.head = Node(val)

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        if index == 0:
            return self.addAtHead(val)
        i = 0
        while i < index:
            if not node:
                return  
            if i == index - 1:
                temp = node.next
                node.next = Node(val)
                node.next.next = temp
                break
            node = node.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        node = self.head
        i = 0
        while i < index:
            if not node:
                return 
            if i == index - 1:
                if node.next:
                    node.next = node.next.next
                break
            node = node.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)