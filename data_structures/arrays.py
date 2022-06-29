"""
Arrays: list in python
- Access: O(1)
- Search: O(N)
- Insert (True Insert, Append, Extend): O(N)
- Delete: O(N)
"""
new_list = [1, 2, 3, 4]

# Search
if 1 in new_list: print(True) # Linear Search

# Alternative search approach, doing the same linear search
for el in new_list:
    if el == 1:
        print(True)
        break

# Inserting:
# True insert - insert an element anywhere in the list using an index value (Linear Runtime)
# Appending - add the item to the end of the list (Constant Time), but dependent on language
# Extend - Ability to add 1 list to another

append_list = [] # here space alocated for the list is 1
print(len(append_list)) # it will give 0, because space used by the list is empty

append_list.append(1) # Here it will easily insert an element to the end of the list
print(len(append_list)) # Now memory allocation & size of the list is same which is 1

append_list.append(2) # Now memory allocation is 1, but it needs to insert 1 more. It increases the size by calling list resize. Growth pattern in python is 0, 4, 8, 16, 25, 35, 46.... means when list size reaches these specific values list resize is called again
# It looks like append method have non constant space complexity
# But some operation don't increase size & some do, so while we average it out. It has constant space complexity: Ammortized Constant Space Complexity

# Resize happens with resize too, but it is more expecnsive because after every insert every element needs to be shifted 1

# Extend makes a series of append call to the original list to add each element from the new list
# It has a complexity of O(K): K is number of elements in new list


# Deletion:
# Similar to insert, but it shifts element to left unlike insert which shifts elements to right
# Linear runtime: O(N)