class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
            self.tail = temp.next
        
    def display(self):
        temp = self.head
        while temp:
            print(f"[{temp.value}] =>", end=" ")
            temp = temp.next
    
    def delete_last(self):
        temp = self.head
        while temp.next and temp.next!= self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
            

ll = linklist()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.display()
ll.delete_last()    
print()
ll.display()    
    