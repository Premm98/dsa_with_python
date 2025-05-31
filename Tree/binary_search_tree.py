class BinarySearchTree():

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value):
        """
        add child to the tree
        """

        if value == self.value:
            print("Dupllicateeeeee insertion", value)
            return
        
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.add_child(value)

        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.add_child(value)


    def print_tree_inorder(self):
        """print tree"""
        if self.left:
            self.left.print_tree_inorder()
        print(self.value, end=' ')
        if self.right:
            self.right.print_tree_inorder()

root = BinarySearchTree(50)
root.add_child(30)
root.add_child(70)
root.add_child(20)
root.add_child(40)
root.add_child(60)
root.add_child(70)  # duplicate
root.add_child(80)

print("In-order Traversal:")
root.print_tree_inorder()