l1 = [0] * 10

print(f"l1 list: {l1}\n")

l2 = [[]] * 10

print(f"Empty list inside list l2: {l2}\n")

# append 1 to first indexed list to l2
l2[0].append(1)

print(f"l2 after appending 1 to first indexed list: {l2}\n")

# elements of l2 keeps reference to empty list, and when we append something whole references takes the same value

# to overcome this, we need to create new list reference in e=very index

l3 = [[] for _ in range(10)]
# append 1 to first indexed list to l3
l3[0].append(1)

print(f"l3 after appending 1 to first indexed list: {l3}\n")

# l1 list: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Empty list inside list l2: [[], [], [], [], [], [], [], [], [], []]

# l2 after appending 1 to first indexed list: [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

# l3 after appending 1 to first indexed list: [[1], [], [], [], [], [], [], [], [], []]
