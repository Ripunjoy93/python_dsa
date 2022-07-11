"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
"""
import sys
from binary_search import binary_search
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def find_num_rotations(rot_list):
    """
    Rotated list
    Conditions:
    1. Will use standard binary search
    2. If list is rotated N times, then output will be 0 as it is already ascending order & we need to find minimum
    3. For empty list, it will be 0
    4. For list with 1 element it will be 0

    Args:
        rot_list (List): It can be any length
        return: number of rotations
    """
    last_index = len(rot_list) - 1
    def condition(mid):
        """
        Time complexity is again O(log N)
        """
        if mid > 0 and rot_list[mid-1] > rot_list[mid]:
            return "found"
        elif rot_list[mid] > rot_list[last_index]:
            return "right"
        else:
            return "left"
    
    res = binary_search(0, last_index, condition)
    if res == -1:
        res = 0
    return res


test_cases = [
    {
        'input': {
            'rot_list': [5, 6, 7, 0, 1, 2, 3, 4],
        },
        'output': 3
    },

    {
        'input': {
            'rot_list': [3, 4, 5, 6, 7, 0, 1],
        },
        'output': 5
    },

    {
        'input': {
            'rot_list': [],
        },
        'output': 0
    },

    {
        'input': {
            'rot_list': [1],
        },
        'output': 0
    },

    {
        'input': {
            'rot_list': [1, 2, 3, 4, 5],
        },
        'output': 0
    },

    {
        'input': {
            'rot_list': [6, 6, 6, 1, 2, 3, 3],
        },
        'output': 3
    },

    {
        'input': {
            'rot_list': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4],
        },
        'output': 6
    }
]

evaluate_test_cases(find_num_rotations, test_cases)
