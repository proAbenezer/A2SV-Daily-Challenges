# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self):
        self.head = None    

    def get(self, index: int) -> int:
        position = 0  
        current = self.head 
        while position < index and current:
            current = current.next
            position += 1
        
        if not current:
            return -1
        return current.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        
        if not self.head:
            self.head = newNode
            return 

        current = self.head
        
        while current.next:
            current = current.next
        current.next = newNode
      
       

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
          self.addAtHead(val)
          return 
        
        position = 0
        current = self.head
        newNode = ListNode(val)

     
        while position < index - 1 and current:
            current = current.next
            position += 1

        if not current:
            return
            
        temp = current.next
        current.next = newNode
        newNode.next = temp
       

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if not self.head:
                return 
            self.head = self.head.next

        position = 0 
        current = self.head 
        while position < index - 1 and current:
            current = current.next
            position += 1

        if not current or not current.next:
            return 
        current.next = current.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)