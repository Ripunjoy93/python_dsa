class BSTNodeUnbalanced():
    """
    A binary search tree or BST is a binary tree that satisfies the following conditions:
    - The left subtree of any node only contains nodes with keys less than the node's key
    - The right subtree of any node only contains nodes with keys greater than the node's key
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def insert(self, key, value):
        """
        Starting from the root node, we compare the key to be inserted with the current node's key
        If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
        If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.
        """
        if self is None:
            self = BSTNodeUnbalanced(key, value)
        elif key < self.key:
            self.left = BSTNodeUnbalanced.insert(self.left, key, value)
            self.left.parent = self
        elif key > self.key:
            self.right = BSTNodeUnbalanced.insert(self.right, key, value)
            self.right.parent = self
        return self

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return BSTNodeUnbalanced.find(self.left, key)
        if key > self.key:
            return BSTNodeUnbalanced.find(self.right, key)

    def update(self, key, value):
        target = BSTNodeUnbalanced.find(self, key)
        if target is not None:
            target.value = value

    def list_all(self):
        if self is None:
            return []
        return BSTNodeUnbalanced.list_all(self.left) + [(self.key, self.value)] + BSTNodeUnbalanced.list_all(self.right)


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNodeUnbalanced(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root
