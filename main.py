from structure import Binary_tree

if __name__ == '__main__':
    Tree = Binary_tree()

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(1)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(13)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(0)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(10)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(3)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(-5)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(-2)

    print("--------------------------")
    print(Tree.print_binary_tree())
    Tree.add(2)
        

    if Tree.search(2) == False:
        print("There isn't this element")
    else:
        print("There is this element")
    
    print("--------------------------")
    print(Tree.print_binary_tree())
    print("--------------------------")
    Tree.delete(1)
    print("--------------------------")
    print(Tree.print_binary_tree())
    print("--------------------------")

