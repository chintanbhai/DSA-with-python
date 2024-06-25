class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack():
    
    def __init__(self):
        self.top = None
       
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def display(self):
        temp = self.top
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        
    def pop(self):
        if self.top is None:
            return
        self.top = self.top.next
        

s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.display()
# s.pop()
# s.display()
while True:
    inp = int(input('\n\nEnter Your choice: \n1.Insert\n2.Display\n3.Delete Last'))
    
    if inp == 1:
        value = int(input('Enter the value: '))
        s.push(value)
    elif inp == 2:
        s.display()
    elif inp == 3:
        s.pop()
        s.display()
    else:
        break