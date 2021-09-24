class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class Binary_tree:

    def __init__(self):
        self.head = None
        
    
    def search(self, data):

        new_Node = Node(data)
        
        if self.head == None:
            return False
        else:
            current = self.head

            while current != None:
                if new_Node.data == current.data:
                    return current
                if new_Node.data > current.data:
                    if current.right == None:
                        return False
                    else:
                        current = current.right
                if new_Node.data < current.data:                    
                    if current.left == None:
                        return False    
                    else:
                        current = current.left


    def print_children(self, current, arr):
        
        if current.right != None:            
            arr.append(current.right.data)            
        if current.left != None:
            arr.append(current.left.data)
                    
        if current.right != None:
            self.print_children(current.right, arr)
        if current.left != None:
            self.print_children(current.left, arr)        
        
    
    def print_binary_tree(self):
        arr = []
        if self.head == None:
            print("There is nothing to print")
            
        else:
            arr.append(self.head.data)
            self.print_children(self.head, arr)
        
        return(arr)


    def add_Node(self, current, data):

        new_Node = Node(data)

        if current.data < data:
            if current.right == None:
                current.right = new_Node
                new_Node.parent = current
                
            else:
                current = current.right
                self.add_Node(current, data)
        else:
            if current.left == None:
                current.left = new_Node
                new_Node.parent = current
                
            else:
                current = current.left
                self.add_Node(current, data)
        

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.add_Node(self.head, data)
    

    def delete_Node(self, current):

            if current == self.head and current.right == None and current.left == None:
                self.head = None
                return 0
            
            elif current == self.head and current.right == None and current.left != None:
                self.head = current.left
                return 0

            elif current == self.head and current.right != None and current.left == None:
                self.head = current.right
                return 0

            elif current != self.head and current.right == None and current.left == None:
                if current.parent.right == current:
                    current.parent.right = None
                elif current.parent.left == current:
                    current.parent.left = None
                
                return 0

            elif current != self.head and current.right == None and current.left != None:
                if current.parent.right == current:
                    current.parent.right = current.left
                    current.left.parent = current.parent
                    
                elif current.parent.left == current:
                    current.parent.left = current.left
                    current.left.parent = current.parent

                return 0
            
            elif current != self.head and current.right != None and current.left == None:
                if current.parent.right == current:
                    current.parent.right = current.right
                    current.right.parent = current.parent
                    
                elif current.parent.left == current:
                    current.parent.left = current.right
                    current.right.parent = current.parent
                
                return 0
            
            elif current.right != None and current.left != None:
                current.data = current.right.data                
                self.delete_Node(current.right)
                
                    
    def delete(self, data):
        if self.head == None:
            print("This object doesn't exist in this structure")
        else:            
            if self.search(data) == False:
                print("This object doesn't exist in this structure")
            else:               
                current = self.search(data)
                self.delete_Node(current)


    def delete_all_elements(self):
        self.head = None
