# Data Structure and Algorithms in Python

## Notes

### Data Structures

1. Arrays: in python it is kind of list defined by [], hetergeneous memory location unlike other programming languages. But python makes it contiguous by saving the memory reference of the array element in the array instead of saving the element itself.
2. Say, 'a' in ['a', 'b', 'c'] code does a Linear Search operation. If sorted then we could have run binary search but that incurs a cost again. So, languages mainly focuses on linear search operations if the array is small.
3. Specific Data Structures can solve specific problems. We can create our own data structures.
4. Say arrays: pretty good at accessing because O(1). But bad at inserting and deleting which is O(N)
5. LinkedList is better than arrays in inserting & deleting but have some caveats. But if we do a lot of insert & delete & few access. LinkedList will be a better choice.

### Algorithms

1. The maximum recursion depth in Python is 1000. [READ](https://www.codingem.com/python-maximum-recursion-depth/#:~:text=Python%20uses%20a%20maximum%20recursion,and%20infinite%20recursions%20are%20possible)
2. Big O Notation. [READ](https://www.bigocheatsheet.com/)
3. Binary Search space complexity is constant O(1), first & last (high & low) index being updated.
4. Recursive version of binary search is O(log N). But here language also plays a role. In python maximum recursion depth is 1000. Python don't have tail call optimization life Swift.
5. In python iterative binary search will be a better choice.
