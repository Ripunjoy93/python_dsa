"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5
"""


import sys
from binary_search import binary_search
sys.path.append(".")

from utils.test_utils import evaluate_test_cases


def rotated_list_locate_number(rot_list, num):
    """
    Convert the list into 2 sorted list
    Search the index in the list

    Args:
        rot_list (List): _description_
        num (int): _description_

    Returns:
        _type_: _description_
    """
    last_index = len(rot_list) - 1
    # def condition1(mid):
    #     if rot_list[mid] == num:
    #         # handle duplicates
    #         if mid > 0 and rot_list[mid-1] == num:
    #             return "left"
    #         else:
    #             return "found"
    #     elif rot_list[mid]< num and num < rot_list[last_index]:
    #         return "right"
    #     else:
    #         return "left"

    # def condition2(mid):
    #     if rot_list[mid] == num:
    #         # handle duplicates
    #         if mid > 0 and rot_list[mid-1] == num:
    #             return "left"
    #         else:
    #             return "found"
    #     elif rot_list[mid] < num and num < rot_list[last_index]:
    #         return "right"
    #     else:
    #         return "left"
    
    # res = binary_search(0, last_index, condition1)

    # if res == -1 and len(rot_list) > 0 and num in rot_list:
    #     print(rot_list)
    #     res = binary_search(0, last_index, condition2)

    def list_break_condition(mid):
        if mid > 0 and rot_list[mid-1] > rot_list[mid]:
            return "found"
        elif rot_list[mid] > rot_list[last_index]:
            return "right"
        else:
            return "left"

    res = binary_search(0, last_index, list_break_condition)

    sorted_list_asc = []
    def asc_list_locate_number_condition(mid):
        if sorted_list_asc[mid] == num:
            if mid > 0 and sorted_list_asc[mid-1] == num:
                return 'left'
            else:
                return 'found'
        elif sorted_list_asc[mid] > num:
            return 'left'
        else:
            return 'right'

    if len(rot_list) > 0:
        check = False
        if res == -1:
            sorted_list_asc = rot_list
        else:
            list1 = rot_list[:res]
            list2 = rot_list[res:]
            if num in list1:
                sorted_list_asc = list1
            else:
                sorted_list_asc = list2
                check = True
        
        res = binary_search(0, len(sorted_list_asc)-1,
                            asc_list_locate_number_condition)
        if check:
            res += len(list1)
            
    return res


test_cases = [
    {
        'input': {
            'rot_list': [5, 6, 7, 0, 1, 2, 3, 4],
            'num': 6
        },
        'output': 1
    },

    {
        'input': {
            'rot_list': [3, 4, 5, 6, 7, 0, 1],
            'num': 0
        },
        'output': 5
    },

    {
        'input': {
            'rot_list': [],
            'num': 5
        },
        'output': -1
    },

    {
        'input': {
            'rot_list': [1],
            'num': 2
        },
        'output': -1
    },

    {
        'input': {
            'rot_list': [1, 2, 3, 4, 5],
            'num': 2
        },
        'output': 1
    },

    {
        'input': {
            'rot_list': [6, 6, 6, 1, 2, 3, 3],
            'num': 6
        },
        'output': 0
    },

    {
        'input': {
            'rot_list': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4],
            'num': 3
        },
        'output': 9
    }
]

evaluate_test_cases(rotated_list_locate_number, test_cases)
