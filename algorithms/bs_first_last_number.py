"""
Question: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

This differs from the problem in only two significant ways:

The numbers are sorted in increasing order.
We are looking for both the increasing order and the decreasing order.
"""

import sys
from binary_search import binary_search
sys.path.append(".")

from utils.test_utils import evaluate_test_cases


def find_first_position(sorted_list_asc, number):

    def condition(mid):
        if sorted_list_asc[mid] == number:
            if mid > 0 and sorted_list_asc[mid-1] == number:
                return "left"
            else:
                return "found"
        elif sorted_list_asc[mid] < number:
            return "right"
        else:
            return "left"
    
    return binary_search(0, len(sorted_list_asc)-1, condition)


def find_last_position(sorted_list_asc, number):

    def condition(mid):
        if sorted_list_asc[mid] == number:
            if mid < len(sorted_list_asc)-1 and sorted_list_asc[mid+1] == number:
                return "right"
            else:
                return "found"
        elif sorted_list_asc[mid] < number:
            return "right"
        else:
            return "left"

    return binary_search(0, len(sorted_list_asc)-1, condition)


def find_first_last_position(sorted_list_asc, number):
    return (find_first_position(sorted_list_asc, number), find_last_position(sorted_list_asc, number))


test_cases = [
    {
        'input': {
            'sorted_list_asc': [-1, 2, 6, 7, 9],
            'number': 6
        },
        'output': (2, 2)
    },

    {
        'input': {
            'sorted_list_asc': [2, 3, 4, 6, 6, 6, 6, 7, 8],
            'number': 6
        },
        'output': (3, 6)
    },

    {
        'input': {
            'sorted_list_asc': [],
            'number': 2
        },
        'output': (-1, -1)
    },

    {
        'input': {
            'sorted_list_asc': [-1, 2, 4, 6, 7, 10],
            'number': 8
        },
        'output': (-1, -1)
    }
]

evaluate_test_cases(find_first_last_position, test_cases)