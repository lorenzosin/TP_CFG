import re
import networkx as nx

string = "Ciao sono lorenzo"
saluto,verbo,nome = re.split(" ",string)
print(saluto)
print(verbo)
print(nome)

G = nx.DiGraph()
G.add_node("Lol", label="Tusco")
print(G.nodes.data())

G.add_edge("Lol","Pizza", label = "Tusco2")
print(G.nodes.data())
