# Create/Declare a Node of a Binary Tree
# Node structure
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

print(firstNode.left.val)

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def inOrder(node, res):
    if node is None:
        return

    # Traverse the left subtree first
    inOrder(node.left, res)

    # Visit the current node
    res.append(node.data)

    # Traverse the right subtree last
    inOrder(node.right, res)

# Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
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
inOrder(root, res)

for node in res:
    print(node, end=" ")