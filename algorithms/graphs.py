class Graph:

    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def add_edge(self, edge):
        n1 = edge[0]
        n2 = edge[1]

        self.data[n1].append(n2)
        self.data[n2].append(n1)

    def remove_edge(self, edge):
        n1 = edge[0]
        n2 = edge[1]

        self.data[n1].remove(n2)
        self.data[n2].remove(n1)

    def __repr__(self):
        return "\n".join(["{}: {} ".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


class GraphMatrix:

    def __init__(self, num_nodes, edges):

        self.num_nodes = num_nodes
        self.data = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1

    def add_edge(self, edge):
        n1, n2 = edge

        self.data[n1][n2] = 1
        self.data[n2][n1] = 1

    def remove_edge(self, edge):
        n1, n2 = edge

        self.data[n1][n2] = 0
        self.data[n2][n1] = 0

    def __repr__(self):
        return "\n".join(["{}".format(neighbors)for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


class GraphGeneral:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3

        self.data = [[] for _ in range(num_nodes)]
        if self.weighted:
            self.weight = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)

                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)

                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}:{}\n".format(i, list(zip(nodes, weights)))

        else:
            for i, nodes in enumerate(self.data):
                result += "{}:{}\n".format(i, nodes)

        return result
    

def bfs(graph, root):
    """
    1  procedure BFS(G, root) is
    2      let Q be a queue
    3      label root as discovered
    4      Q.enqueue(root)
    5      while Q is not empty do
    6          v := Q.dequeue()
    7          if v is the goal then
    8              return v
    9          for all edges from v to w in G.adjacentEdges(v) do
    10              if w is not labeled as discovered then
    11                  label w as discovered
    12                  Q.enqueue(w)
    """
    discovered = [False] * len(graph.data)
    queue = []

    distance = [None] * len(graph.data)

    queue.append(root)
    discovered[root] = True
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                discovered[node] = True
                queue.append(node)
    return queue


def is_connected(num_nodes, edges, root=0):
    graph = Graph(num_nodes, edges)
    queue, distance, parent = bfs(graph, root)

    queue_size = len(queue)

    if queue_size < num_nodes:
        return "Not Connected"
    else:
        return 'connected'


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.insert(0, node)

    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier.remove(node)
            return node

    def top(self):
        return self.frontier[0]

    def __len__(self):
        return len(self.frontier)

    def __repr__(self):
        return str(self.frontier)


def dfs(graph, root):
    discovered = [False] * len(graph.data)
    stack = StackFrontier()
    result = []

    stack.add(root)

    while len(stack) > 0:
        current = stack.remove()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)

            for node in graph.data[current]:

                if not discovered[node]:
                    stack.add(node)

    return result


def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    """Pick the next unvisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0

    queue.append(source)
    distance[source] = 0
    visited[source] = True

    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        print("parent", parent)
        update_distances(graph, current, distance, parent)

        next_node = pick_next_node(distance, visited)
        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        idx += 1

    return distance[dest], distance, parent

