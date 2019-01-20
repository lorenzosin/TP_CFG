import re
from networkx import *


def find_succ(G, node, path=[]):
    path += [node]

    for i in G.adj(node):
        if i not in path:
            path = find_succ(G, i, path)

    return path


G = nx.DiGraph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "E")
G.add_edge("E", "F")


# print(G.nodes)
# print(G.node("A"))
# print(G.nodes("A"))

# print(list(G.successors("A")))

print(find_succ(G, "A", "A"))


# n = G.successors("A")
# for i in n:
#     print(i)
