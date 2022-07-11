class BinaryTreeNode:
    """
    Implementation of Binary tree in python
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node key: {self.key}"


# node0 = BinaryTreeNode(4)
# node1 = BinaryTreeNode(3)
# node2 = BinaryTreeNode(5)

# node0.left = node1
# node0.right = node2

# root = node0

# print(root)
# print(root.left)
# print(root.right)