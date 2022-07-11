import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def insertion_sort(nums):
    """
    Keep the initial portion of the array sorted and insert the remaining elements one by one at the right position.
    """
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        # This while loop ends either when it comes to index 0 and current become greater than previous number in the list
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


test_cases = [
    {
        'input': {
            'nums': [4, 2, 6, 3, 4, 6, 2, 1]
        },
        'output': [1, 2, 2, 3, 4, 4, 6, 6]
    },
    {
        'input': {
            'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
        },
        'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
    },
    {
        'input': {
            'nums': [3, 5, 6, 8, 9, 10, 99]
        },
        'output': [3, 5, 6, 8, 9, 10, 99]
    },
    {
        'input': {
            'nums': [99, 10, 9, 8, 6, 5, 3]
        },
        'output': [3, 5, 6, 8, 9, 10, 99]
    },
    {
        'input': {
            'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
        },
        'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
    },
    {
        'input': {
            'nums': []
        },
        'output': []
    },
    {
        'input': {
            'nums': [23]
        },
        'output': [23]
    },
    {
        'input': {
            'nums': [42, 42, 42, 42, 42, 42, 42]
        },
        'output': [42, 42, 42, 42, 42, 42, 42]
    }
]

evaluate_test_cases(insertion_sort, test_cases)
