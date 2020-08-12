from collections import defaultdict


class Node:
    def __init__(self):
        self.neighbours = set()
        self.attributes = defaultdict()


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value: int):
        """Add a new node to the graph"""
        node = Node()

        self.nodes[value] = node

    def add_edge(self, src, dest):
        """Add an edge to a node"""
        self.nodes[src].neighbours.add(dest)
        self.nodes[dest].neighbours.add(src)

    def add_edge_list(self, lst: list):
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

    def degree(self, value):
        """Compute the degree for a node"""
        return len(self.nodes[value].neighbours)

    def __repr__(self):
        return f"<Graph>"


if __name__ == '__main__':
    graph = Graph()

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(4)
    graph.add_node(3)

    graph.add_edge(1, 2)
    graph.add_edge_list([(2, 4), (1, 3)])

    print(graph.nodes[1].neighbours)
    print(graph.nodes[2].neighbours)

    print(graph.degree(3))

    graph.add_attribute(1, {"age": 12, "city": "Tehran"})
    for i in graph.adjacency_list(1):
        print(i)

    print(graph.nodes[1])