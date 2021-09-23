class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Binary_tree:

    def __init__(self):
        self.head = None

    def add(self, data):

        new_Node = Node(data)

        if self.head == None:
            self.head = new_Node

        else:
            current = self.head
            while current:
                while current.right or current.left :
                    if current.data < new_Node.data:
                        current = current.right
                    else:
                        current = current.left                

                if current.data < new_Node.data:
                    current.right = new_Node
                    new_Node.parent = current
                else:
                    current.left = new_Node
                    new_Node.parent = current
    
    def search(self, data):

        new_Node = Node(data)
        
        if self.head == None:
            return False
        else:
            current = self.head

            while current:
                if new_Node.data == current.data:
                    return True
                elif new_Node.data > current.data:
                    current = current.right
                    if current.right and current.left == None:
                        return False
                elif new_Node.data < current.data:
                    current = current.left
                    if current.right and current.left == None:
                        return False    
                

    def delete(self, data):

        new_Node = Node(data)

        if self.search(data) == False:
            print("This object doesn't exist in this structure")
        else:
            current = self.head
            while current.right or current.left:
                if new_Node.data == current.data:
                    
                    if current.right == None:
                        current.parent.right = current.right
                    while current.right:
                        current.parent.right = current.right
                        current = current.right
                        
                elif new_Node.data > current.data:
                    current = current.right

                elif new_Node.data < current.data:
                    current = current.left


    def print_children(self, current):
        current_right = current.right
        current_left = current.left
        print(current_right)
        print(current_left)
        

    def print_binary_tree(self):
        if self.head == None:
            print("There is nothong to print")
        else:
            print(self.head.data)
        self.print_children()
