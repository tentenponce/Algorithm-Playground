def print_edges(edges):
    if len(edges) > 0:
        for edge in edges:
            print("neighbor: " + edge.name)


def traverse(graph):
    for key in graph:
        n = graph[key]

        print(key)
        if n.parent is not None:
            print("parent: " + n.parent.name)
        print_edges(n.edges)
        print()
