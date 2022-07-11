'''
Following codes gives basic structure of binary search
It can work with any coditions
Whenever some algorithms comes up we can use function closure of python
Which is function inside a function
'''


def binary_search(lo: int, hi: int, condition) -> int:
    """
    Basic implementations of binary search

    Args:
        lo (int): low index or number
        hi (int): high index or number
        condition (function): will be used in function closure

    Returns:
        int: _description_
    """
    while lo<=hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result=='found':
            return mid
        elif result=='left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# print(binary_search.__annotations__)

