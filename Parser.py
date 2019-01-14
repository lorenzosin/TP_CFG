# Using NetworkX as library for the creation of Graphs
import networkx as nx
# Using re = regular expressions for the lines parsing
import re
# Using os to run terminal command for the conversion dot -> pdf
import os
# Using graph to generate the dot file
from graphviz import Digraph

# I am assming that the file exists and user has permissions -> No checks
f = open("out.txt", "r")

# Research for the main block
end_lecture = 0  # Flag external loop
end_main = 0  # Flag internal loop for main
code = []  # Where to put the main block
while end_lecture == 0:
    row = f.readline()
    useful = row.find("<main>:")  # Searching starting point
    if (useful != -1):
        # code.append(row.strip())
        while end_main == 0:
            row = f.readline()
            if row == "\n":  # Searching ending point (empity line)
                end_main = 1
                end_lecture = 1
            else:
                code.append(row.strip())  # Strip() removes the extra \n

# Closure of the file
f.close()

# Display of the code
# for i in code:
#     print(i)

graph = nx.DiGraph()
graph.clear()
len(code)
instr_set = []
for i in range(0, len(code)):
    prev_is_branch = 0  # Flag used to manage the targets
    if((i + 1) < len(code)):  # Still not the last row
        # First line of the pair
        prev_parsed = re.split("\t", code[i])
        prev_address = prev_parsed[0]     # take first element
        prev_address = prev_address[:-1]  # remove the ':' character
        prev_name = prev_parsed[1]
        prev_instruction = prev_parsed[2]
        prev_arguments = prev_parsed[3]

        if (prev_address not in graph.nodes()):
            graph.add_node(prev_address)

        if (prev_instruction[0]) == "b":
            # There could be the target name
            prev_target = prev_parsed[3].split(" ")
            # print("branch to " + str(target[0]))
            if (str(prev_target[0]) not in graph.nodes()):
                graph.add_node(str(prev_target[0]))
                graph.add_edge(prev_address, str(prev_target[0]))
                prev_is_branch = 1

        # Following line
        parsed = re.split("\t", code[i + 1])
        address = parsed[0]     # take first element
        address = address[:-1]  # remove the ':' character
        name = parsed[1]
        instruction = parsed[2]
        arguments = parsed[3]

        # Adding the new node, if not already discovered
        if(address not in graph.nodes()):
            graph.add_node(address)

        # Connect the previous instruction with the following one, if the case
        if(prev_is_branch == 0):
            graph.add_edge(prev_address, address)

        if (instruction[0]) == "b":
            target = parsed[3].split(" ")   # There could be the target name
            if (str(target[0]) not in graph.nodes()):
                graph.add_node(str(target[0]))
            graph.add_edge(address, str(target[0]))

        if prev_instruction not in instr_set:
            instr_set.append(prev_instruction)
        if instruction not in instr_set:
            instr_set.append(instruction)

    else:   # This is the last row
        parsed = re.split("\t", code[i])
        address = parsed[0]     # take first element
        address = address[:-1]  # remove the ':' character
        name = parsed[1]
        instruction = parsed[2]
        arguments = parsed[3]
        graph.add_node(address)
        if (instruction[0]) == "b":
            target = parsed[3].split(" ")   # There could be the target name
            # print("branch to " + str(target[0]))
        if instruction not in instr_set:
            instr_set.append(instruction)
        graph.add_node(str(target[0]))
        graph.add_edge(address, str(target[0]))

    # print(graph.nodes)
#
# for i in graph.nodes():
#     if((list(graph.neighbors(i)).count) == 0):
print("#############################################")
print("#### Assembly Parser - CFG Reconstructor ####")
print("#############################################")
print("Instruction Set:")
for i in instr_set:
    print("\t" + str(i))

graph.number_of_nodes()
nodes = sorted(graph.nodes())
print("\nList of adjacent nodes:")
for i in nodes:
    print("\tNode " + str(i) + " --> " + str(list(graph.neighbors(i))))

# Generate the new dot file
# WriteDot("CFG.dot", graph)
# dot = Digraph("Reconstructed CFG")
# for i in graph.nodes():
#     dot.node(i)
#
# for i in graph.edges():
#     print(i)
#
# print(dot.source)
#
# dot.render("CFG")


# def WriteDot(fout, graph):
print("Generating output file CFG.dot..")
f = open("CFG.dot", "w")
f.write("digraph ReconstructedCFG {\n")
for i in nodes:
    # f.write("\t" + i + " [ label = \"" + i + "\" ];\n")
    f.write("\t\"" + i + "\";\n")
    neigh = list(graph.neighbors(i))
    for j in range(len(neigh)):
        f.write("\t\"" + str(i) + "\" -> \"" + neigh[j] + "\";\n")
f.write("}")
f.close()

print("Generating output file CFG.dot..")
os.system("dot -Tps CFG.dot -o CFG.pdf")
