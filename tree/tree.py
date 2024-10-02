class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self):
        self.root = None
        self.prev = None
        self.successor = None
        
    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val)
        else:
            temp = self.root
            while True:
                if new_val < temp.data:
                    if temp.left is None:
                        temp.left = Node(new_val)
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(new_val)
                        break
                    else:
                        temp = temp.right
    
    def pre_order(self, root):
        if root is None:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)
    
    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)
        
    def delete(self, value):
        temp = self.root
        self.prev = None
        isleft = 0

        # Traverse to find the node to delete
        while temp is not None:
            if value == temp.data:
                break
            elif value < temp.data:
                self.prev = temp
                temp = temp.left
                isleft = 1
            else:
                self.prev = temp
                temp = temp.right
                isleft = 0

        if temp is None:
            print("Data Not Found")
            return

        if temp.left is None and temp.right is None:
            if temp == self.root:
                self.root = None
            elif isleft:
                self.prev.left = None
            else:
                self.prev.right = None

        elif temp.left is None or temp.right is None:
            if temp.left is not None:
                temp2 = temp.left
            else:
                temp2 = temp.right

            if temp == self.root:
                self.root = temp2
            elif isleft:
                self.prev.left = temp2
            else:
                self.prev.right = temp2

        # Case 3: Node to delete has two children
        else:
            # Find the in-order successor (smallest node in the right subtree)
            self.successor = temp.right
            self.prev = temp

            # Find leftmost child of the right subtree (in-order successor)
            while self.successor.left is not None:
                self.prev = self.successor
                self.successor = self.successor.left

            # Replace data of temp with successor's data
            temp.data = self.successor.data

            # Now, delete the successor node (successor has at most one right child)
            if self.successor.right is not None:
                if self.prev.left == self.successor:
                    self.prev.left = self.successor.right
                else:
                    self.prev.right = self.successor.right
            else:
                if self.prev.left == self.successor:
                    self.prev.left = None
                else:
                    self.prev.right = None

                


ch = 0
bt = BinaryTree()

while ch != 6:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    ch = int(input("Enter Your Choice:\n1. Insert\n2. Pre Order Traversal\n3.in Order Traversal\n4. Post Order Traversal\n5. Dalete\n6.Exit\n"))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if ch == 1:
        val = int(input("Enter the value: "))
        bt.insert(val)
    elif ch == 2:
        bt.pre_order(bt.root)
    elif ch == 3:
        bt.in_order(bt.root)
    elif ch == 4:
        bt.post_order(bt.root)
    elif ch == 5:
        val = int(input("Enter The Value:"))
        bt.delete(val)
    elif ch == 6:
        break
    else:
        print("Invalid Choice")