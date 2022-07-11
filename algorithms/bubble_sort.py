import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def bubble_sort(nums):
    """
    There are two loops, each of length n-1, where n is the number of elements in nums. So the total number of comparisons is (n-1) * (n-1)
    - Time complexity O(N^2)
    - space complexity of bubble sort is O(N), even thought it requires only constant/zero additional space O(1), because the space required to store the inputs is also considered while calculating space complexity.
    """
    
    # Create a copy of the list, to avoid changing it
    nums = list(nums)

    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):

        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):

            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
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

evaluate_test_cases(bubble_sort, test_cases)