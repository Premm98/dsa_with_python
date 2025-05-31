class Tree():
    """
    This is the Tree class for demontration a
    Tree Data Structure
    """

    def __init__(self, value):
        self.node = value
        self.children = []

    def add_child(self, child):
        """
        Add child to the node
        """
        child = Tree(child)
        self.children.append(child)
        return child
    
root = Tree("A")
node_b = root.add_child("B")
node_c = root.add_child("C")
node_d = root.add_child("D")

node_b.add_child("E")
node_b.add_child("F")

def print_tree(node, level=0):
    print("|_" * level + node.node)
    for child in node.children:
        print_tree(child, level + 1)

# Print the tree
print_tree(root)