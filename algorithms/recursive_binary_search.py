def recursive_binary_search(input_list, condition):

    #TODO: Verify if this logic is true, if not follow: https://teamtreehouse.com/library/introduction-to-algorithms/algorithms-in-code/binary-search-implementations

    #TODO: Python have maximum recursion depth: 1000: https://www.codingem.com/python-maximum-recursion-depth/#:~:text=Python%20uses%20a%20maximum%20recursion,and%20infinite%20recursions%20are%20possible.
    
    if len(input_list) == 0:
        return -1
    
    mid = len(input_list)//2

    result = condition(mid)

    if result == "found":
        return mid
    elif result == "left":
        return recursive_binary_search(input_list[:mid], condition)
    else:
        return recursive_binary_search(input_list[mid:], condition)