class Node:

    def __init__(self, name):
        self.name = name
        self.edges = []
        self.parent = None  # should be Node

    def connect(self, node):
        self.edges.append(node)
        node.edges.append(self)
