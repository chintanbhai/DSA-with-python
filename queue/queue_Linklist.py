class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        new_node = Node(data)
        
        if self.front == None or self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front == None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()


q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
print("Deleted :",q.dequeue())
q.display()
        