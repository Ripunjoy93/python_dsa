import sys
from binary_search import binary_search
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def locate_number(sorted_list_desc, number):
    """
    Given a list of sorted numbers, we need to return the index of matching numbers
    Args:
        sorted_list_desc (List): integer list in descending order
            - can be empty
            - number need not to be present there
            - number can be there in multiple places
        number (int): number to find
    """
    def condition(mid):
        """
        Function inside a function, it's called function closure

        Here binary search will provide middle value but the condition can also access
        the list, number
        Args:
            mid (int): index
        """
        if sorted_list_desc[mid]==number:
            if mid > 0 and sorted_list_desc[mid-1] == number:
                return 'left'
            else:
                return 'found'
        elif sorted_list_desc[mid] < number:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(sorted_list_desc)-1, condition)


test_cases = [
    {
        'input' : {
            'sorted_list_desc': [9, 7, 6, 4, 2, -1],
            'number': 6
        },
        'output': 2
    },

    {
        'input' : {
            'sorted_list_desc': [9, 7, 7, 6, 6, 6, 6, 4, 2],
            'number': 6
        },
        'output': 3
    },

    {
        'input' : {
            'sorted_list_desc': [],
            'number': 2
        },
        'output': -1
    },

    {
        'input' : {
            'sorted_list_desc': [9, 7, 6, 4, 2],
            'number': 8
        },
        'output': -1
    }
]

evaluate_test_cases(locate_number, test_cases)