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
                self.left.add_child(child)
            else:
                self.right.add_child(child)

    def isfull(self):
        return self.left is not None and self.right is not None
    
    def print_tree(self, root):
        """Print tree"""
        while root.left is None and root.right is None:
            print(root, root.left.value, root.right.value)


root = BinaryTree("A")
root.add_child("B")
root.add_child("C")
root.add_child("D")
root.add_child("E")
root.add_child("F")
root.add_child("G")


def print_tree(node):
    if node is None:
        return

    # Print current node and its children (if any)
    left_val = node.left.value if node.left else "None"
    right_val = node.right.value if node.right else "None"
    print(f"Node: {node.value}, Left: {left_val}, Right: {right_val}")

    # Recurse on left and right
    print_tree(node.left)
    print_tree(node.right)

print_tree(root)
