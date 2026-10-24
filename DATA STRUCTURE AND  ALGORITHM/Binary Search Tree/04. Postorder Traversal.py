class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def postOrder(node, res):
    if node is None:
        return

    # First we traverse left subtree
    postOrder(node.left, res)

    # After visiting left, traverse right subtree
    postOrder(node.right, res)

    # now we visit node
    res.append(node.data)

# Create binary tree
    #        1
    #      /   \
    #    2      3
    #   / \    / \
    #  4   5  7   6
    #            /  \
    #           8    9
               
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.right.right = Node(9)

res = []
postOrder(root, res)

for node in res:
    print(node, end=" ")