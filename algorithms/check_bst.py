import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases
from data_structures.binary_tree import BinaryTreeNode
from data_structures.binary_tree_node import TreeNode

def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key


tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(f"Is tree1 is Binary Search Tree: {is_bst(tree1)}\n")

tree2 = TreeNode.parse_tuple(
    (('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(f"Is tree2 is Binary Search Tree: {is_bst(tree2)}\n")

tree1.display_keys_vertically()

print("*" * 30)

tree2.display_keys_vertically()
