import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases
from data_structures.binary_tree import BinaryTreeNode


# tuple structure in BT: (left, root, right)
tree_data = ((1,3,None),4,((5,6,7), 8, (None, 10, 11)))

def parse_tuple_to_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = BinaryTreeNode(data[1])
        node.left = parse_tuple_to_tree(data[0])
        node.right = parse_tuple_to_tree(data[2])
    elif data is None:
        node = None
    else:
        node = BinaryTreeNode(data)
    return node

tree = parse_tuple_to_tree(tree_data)

print(f"Tuple Tree: \n{tree}\n{tree.left}\n{tree.right}\n")


def parse_tree_to_tuple(node):
    """
    Convert a tree to tuple structure
    """
    if isinstance(node, BinaryTreeNode):
        if node.left is None and node.right is None:
            return node.key
        else:
            return (parse_tree_to_tuple(node.left), node.key, parse_tree_to_tuple(node.right))

tree_tuple = parse_tree_to_tuple(tree)

print(f"Print tuple: \n{tree_tuple}\n")


def display_keys(node, space='\t', level=0):
    """
    Print all the keys of the left and right subtree with proper indentation.
    Visualize the tree that is being created (albeit rotated by 90 degrees)
    """
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

display_keys(tree)


def traverse_in_order(node):
    """
    Traverse the left subtree recursively in-order.
    Traverse the current node.
    Traverse the right subtree recursively in-order.
    Here first in the list will be left side then the middle and the the right side
    """
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


print(f"\nIn-order traversal: {traverse_in_order(tree)}\n")


def traverse_pre_order(node):
    """
    Traverse the current node.
    Traverse the left subtree recursively preorder.
    Traverse the right subtree recursively preorder.
    """
    if node is None:
        return []
    else:
        return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)

print(f"Pre-order traversal: {traverse_pre_order(tree)}\n")


def traverse_post_order(node):
    """
    Traverse the left subtree recursively pre-order.
    Traverse the right subtree recursively pre-order.
    Traverse the current node.
    """
    if node is None:
        return []
    else:
        return traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key]


print(f"Post-order traversal: {traverse_post_order(tree)}\n")


def tree_max_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(tree_max_height(node.left), tree_max_height(node.right))


print(f"Max height of the tree: {tree_max_height(tree)}\n")


def tree_size(node):
    if node is None:
        return 0
    else:
        return 1 + tree_size(node.left) + tree_size(node.right)


print(f"Size of the tree: {tree_size(tree)}\n")
