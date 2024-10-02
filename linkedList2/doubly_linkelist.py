class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, value):
        
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            
    def insert_first(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
    
    def display(self):
        temp = self.head
        while temp:
            print(f"[{temp.value}] =>", end=" ")
            temp = temp.next
    
    
    
    
    

d1 = DoublyLinkedList()
d1.insert(10)
d1.insert(20)
d1.insert(30)
d1.insert(40)
d1.insert(50)
d1.insert(60)
d1.display()
print("\nAfter inserting at first:\n")
d1.insert_first(5)
d1.insert_first(2)
d1.display()
