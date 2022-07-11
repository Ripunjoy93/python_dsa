import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

def merge_sort(nums):
    """
    - Divide the inputs into two roughly equal parts.
    - Recursively solve the problem individually for each of the two parts.
    - Combine the results to solve the problem for the original inputs.
    - Include terminating conditions for small or indivisible inputs.
    Time complexity: O(N log N): O(N) for merge operation and it is invoked O(log N) times
    Space complexity is O(N)
    """
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


def merge(nums1, nums2):
    """
    Time complexity of merge is O(N)
    """
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


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

evaluate_test_cases(merge_sort, test_cases)
