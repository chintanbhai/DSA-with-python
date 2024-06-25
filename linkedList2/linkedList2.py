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
            self.tail.next = Node(value)
            self.tail = self.tail.next
            
    def insert_first(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head = Node(value)
            
            
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
        
    def delete_first(self):
        self.head = self.head.next
        
    def delete_place(self,n):
        temp = self.head
        count = 1
        while temp is not None and count < n - 1:
            temp = temp.next
            count += 1
        print(temp.value)
        if temp is None or temp.next is None:  
            return
        if temp.next == self.tail:  
            self.tail = temp
        temp.next = temp.next.next
            
            
            

    
l1 = linklist()

while True:
    inp = int(input('\n\nEnter Your choice: \n1.Insert\n2.Display\n3.Delete Last\n4.Delete First\n5.Delete place\n6.stop\n'))
    
    if(inp == 1):
        num = int(input("Enter your number :"))
        l1.insert(num)
    elif(inp == 2):
        l1.display()
    elif(inp == 3):    
        l1.delete_last()
    elif(inp == 4):    
        l1.delete_first()
    elif(inp == 5):    
        n = int(input("Enter the position to delete :"))
        l1.delete_place(n)
    elif(inp == 6):
        break