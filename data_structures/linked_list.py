"""
Linear data structure where each element in the list contained in a separate object called Node
- Node: models 2 pieces of info, an individual item that we want to store & a reference to the next Node in the list. Self referencial objects
- First node in the list is HEAD of the list (list keeps reference to the HEAD)
- Last node is TAIL (in some implementations it keeps reference to tail also)
- Two forms: Singly Linked List (refernce to next node) & Doubly Linked List having reference to Node of both before & after
"""

class Node:
    """
    Creating a node which will have data & reference to next node
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


# n1 = Node(10)
# n2 = Node(20)
# n1.next_node = n2
# print(n1.next_node)

class LinkedList:
    """
    Singly linked list: have reference only to head
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Linear Time O(N)
        Returns:
            int: count of nodes
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        """
        Adds a new node containing data to the head of the list
        Now new node becomes the head
        Constant time O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search the list with a key
        Linear time O(N)

        Args:
            key (data): data of the node
        
        Returns:
            First matching Node with key
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)


# l = LinkedList()
# n1 = Node(10)
# l.head = n1
# print(l.size())

# l = LinkedList()
# l.add(10)
# print(l.size())
# l.add(20)
# print(l.size())

# l = LinkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.add(5)
# l.add(6)
# print(l)
# print(l.search(5))
# print(l.search(7))
