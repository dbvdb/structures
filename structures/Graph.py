from collections import defaultdict


class Node:
    def __init__(self, value):
        self.id = value
        self.neighbours = set()
        self.attributes = defaultdict()

    def __repr__(self):
        return f"<{self.id}>"


class Graph:
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def add_node(self, value: int) -> None:
        """Add a new node to the graph"""
        node = Node(value)
        self.nodes[value] = node
        self.size += 1

    def add_edge(self, src, dest) -> None:
        """Add an edge to a node"""
        self.nodes[src].neighbours.add(dest)
        self.nodes[dest].neighbours.add(src)

    def add_edge_list(self, lst: list) -> None:
        """Add a list of edges to the graph"""
        for src, dest in lst:
            self.add_edge(src, dest)

    def add_attribute(self, value, attr: dict) -> None:
        """Add new attributes to a vertex"""
        for k, v in attr.items():
            self.nodes[value].attributes[k] = v

    def adjacency_list(self, value):
        """Create an iterator of neighbours"""
        for node in self.nodes[value].neighbours:
            yield (value, node)

    def degree(self, value) -> int:
        """Compute the degree for a node"""
        return len(self.nodes[value].neighbours)

    def dfs(self):
        """Traverse the graph by depth first search"""
        ...

    def bfs(self):
        """Traverse the graph by breadth first search"""
        ...

    def is_connected(self):
        """Check whether the graph is connected"""
        ...

    def is_empty(self):
        """Check whether the graph is empty"""
        return len(self.nodes) == 0

    def get_vectors(self):
        """Get vectors as an iterator"""
        for vertex in self.nodes.keys():
            yield vertex

    def get_edges(self):
        """Get all edges"""
        ...

    def __contains__(self, vertex):
        return vertex in self.nodes

    def __iter__(self):
        return iter(self.nodes.keys())

    def __repr__(self):
        return f"<Graph>"


if __name__ == '__main__':
    graph = Graph()

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(4)
    graph.add_node(3)
    graph.add_node(5)

    graph.add_edge(1, 2)
    graph.add_edge_list([(2, 3), (4, 5)])

    graph.dfs()

