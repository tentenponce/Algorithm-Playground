from GraphUtil import traverse
from Node import Node
from desserts import desserts

# build graph

dessert_graph = {}

for dessert in desserts:
    group_node = Node(dessert["name"])
    dessert_graph[group_node.name] = group_node

    for member in dessert["members"]:
        member_node = dessert_graph.get(member)

        if member_node is None:
            member_node = Node(member)

        dessert_graph[member_node.name] = member_node
        group_node.connect(member_node)

traverse(dessert_graph)


# define search algorithm

def breadth_first_search(graph, start_node_name, goal_node_name):
    start_node = graph[start_node_name]

    searched = [start_node.name]
    q = [start_node]

    while len(q) > 0:
        node_in_first_q = q.pop(0)

        if node_in_first_q.name == goal_node_name:
            return node_in_first_q

        for edge in node_in_first_q.edges:
            if edge.name not in searched:
                searched.append(edge.name)
                edge.parent = node_in_first_q
                q.append(edge)

    print("Not Found")


#  test breadth first search
found_node = breadth_first_search(dessert_graph, "Nougat", "Banana")

# print path
path = []

while found_node is not None:
    path.append(found_node.name)
    found_node = found_node.parent

print("Path found!")
for p in reversed(path):
    print(p, end="")

    if p is not path[0]:
        print(" --> ", end="")
