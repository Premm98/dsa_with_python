class BinaryTree():

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def add_child(self, child):

        new_node = BinaryTree(child)

        if self.left is None:
            self.left = new_node
        
        elif self.right is None:
            self.right = new_node

        else:
            if not self.left.isfull():
                self.left.add_child(new_node)
            else:
                self.right.add_child(new_node)

    def isfull(self):
        return self.left is not None and self.right is not None


root = BinaryTree("A")
root.add_child("B")
root.add_child("C")
root.add_child("D")
root.add_child("E")
root.add_child("F")
