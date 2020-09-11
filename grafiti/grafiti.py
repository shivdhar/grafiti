class Node:
    def __init__(self, callable_, depends_on=None):
        if not callable(callable_):
            self.callable = callable_

        self.depends_on = depends_on or None
        self.output = None

class Graph:
    def __init__(self):
        self.nodes = []

    @classmethod
    def add_node(callable_, depends_on=None):
        node = Node(callable_, depends_on=depends_on)
        self.nodes.append(node)
        return node
