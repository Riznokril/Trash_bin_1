import unittest
from structure import Binary_tree, Node

class TestBST(unittest.TestCase):
    
    def test_added_element(self):
        BST = Binary_tree()
        BST.add(10)
        test_Node = BST.search(10)
        self.assertEqual(test_Node.data, Node(10).data)

    def test_added_a_few_elements(self):
        BST = Binary_tree()
        BST.add(10)
        BST.add(-10)
        BST.add(0)        
        self.assertEqual(BST.print_binary_tree(), [10, -10, 0])

    def test_deleted_element(self):
        BST = Binary_tree()
        BST.add(15)
        BST.add(23)
        BST.delete(15)
        self.assertEqual(BST.print_binary_tree(), [23])

    def test_print_whole_tree(self):
        BST = Binary_tree()
        BST.add(15)
        BST.add(23)
        self.assertEqual(BST.print_binary_tree(), [15, 23])

    def test_delete_all(self):
        BST = Binary_tree()
        BST.add(15)
        BST.add(23)
        BST.add(-10)
        BST.delete_all_elements()
        self.assertEqual(BST.print_binary_tree(), [])

if __name__ == "__main__":
    unittest.main()
    