class Stack:
    def __init__(self):
        self.top = None
        self.stack = []
        
    def push(self,value):
        if self.top is None:
            self.top = value
            
        
    def display(self): 
        print(self.stack)
        


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
