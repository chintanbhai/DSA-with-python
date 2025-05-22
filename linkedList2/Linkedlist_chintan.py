class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linkedlist_chintan:
    def __init__(self):
        self.head = None
        
    def insert(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        
        
        

s1 = Linkedlist_chintan()