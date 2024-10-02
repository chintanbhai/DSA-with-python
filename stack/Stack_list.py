class Stack:
    def __init__(self):
        self.stack = []  # Initialize the stack as an empty list
        
    def push(self, value):
        self.stack.append(value)  # Append the value to the stack
        
    def display(self):
        print(self.stack)  # Print the current stack
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
