class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def levelOrderRec(root, level, res):
    # Base case
    if root is None:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.data)

    # Recur for left and right children
    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

# Function to perform level order traversal
def levelOrder(root):
    # Stores the result level by level
    res = []
    levelOrderRec(root, 0, res)
    return res
    
    #      5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14    2
    # /  \  /  \  / \
    #17  23 27 3 8  11

root = Node(5)
root.left = Node(12)
root.right = Node(13)

root.left.left = Node(7)
root.left.right = Node(14)

root.right.right = Node(2)

root.left.left.left = Node(17)
root.left.left.right = Node(23)

root.left.right.left = Node(27)
root.left.right.right = Node(3)

root.right.right.left = Node(8)
root.right.right.right = Node(11)

res = levelOrder(root)

for level in res:
        print(' '.join(map(str, level)))