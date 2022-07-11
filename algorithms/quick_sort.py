import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def quicksort(nums, start=0, end=None):
    """
    To overcome the space inefficiencies of merge sort.
    - If the list is empty or has just one element, return it. It's already sorted.
    - Pick a random element from the list. This element is called a pivot.
    - Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, while all elements with values greater than the pivot come after it. This operation is called partitioning.
    - The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.
    """
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

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

evaluate_test_cases(quicksort, test_cases)
