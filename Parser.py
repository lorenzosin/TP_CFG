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
    useful = row.find("<find_min>:")  # Searching starting point
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


# Graph construction
graph = nx.DiGraph()


# Code parsing
code_parsed = []
for i in range(len(code)):
    row = re.split("\t", code[i])
    code_parsed.append(row)

# print(code_parsed)

# for i in range(len(code)):
#     print(code_parsed[i][0])

for i in range(len(code_parsed)):
    addr = code_parsed[i][0]
    code_parsed[i][0] = addr[:-1]


instr_set = []
same_block = []
for i in range(len(code_parsed)):
    addr = code_parsed[i][0]
    same_block.append(addr)
    instr = code_parsed[i][2]
    if instr not in instr_set:
        instr_set.append(instr)

# print(same_block)
# print(instr_set)

l_instr = -1  # Flag until found
for i in range(len(code_parsed)):
    addr = code_parsed[i][0]
    instr = code_parsed[i][2]
    graph.add_node(addr, label=str(instr))
    if instr == "b" or instr == "bx" or instr == "bl":  # Unconditional branch
        tmp = code_parsed[i][3]
        pars = tmp.split(" ")
        n_instr = pars[0]
        if n_instr == "lr":
            l_instr = instr
            l_addr = addr
            break
        else:
            if n_instr in same_block:
                graph.add_edge(addr, n_instr, label="Unconditional branch")
            else:
                graph.add_edge(addr, n_instr, label="Unconditional branch to outer block")
                if i + 1 < len(code_parsed):
                    graph.add_edge(n_instr, code_parsed[i + 1][0], label="Return from outer block")
    else:
        if instr[0] == "b":  # In this branch, only conditional ones remained
            tmp = code_parsed[i][3]
            pars = tmp.split(" ")
            n_instr = pars[0]
            if n_instr == "lr":
                l_instr = instr
                l_addr = addr
                break
            else:
                if n_instr in same_block:
                    graph.add_edge(addr, n_instr, label="taken")
                    if i + 1 < len(code_parsed):
                        graph.add_edge(addr, code_parsed[i + 1][0], label="untaken")
                else:
                    graph.add_edge(addr, n_instr, label="taken to outer block")
                    if i + 1 < len(code_parsed):
                        graph.add_edge(n_instr, code_parsed[i + 1][0], label="Return from outer block")
                        graph.add_edge(addr, code_parsed[i + 1][0], label="untaken")
        else:
            if i + 1 < len(code_parsed):
                graph.add_edge(addr, code_parsed[i + 1][0], label="")

# print(graph.nodes())

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

# Entry Point
print("Generating output file CFG.dot..")
f = open("CFG.dot", "w")
f.write("digraph ReconstructedCFG {\n")
f.write("\t\"Entry Point\";\n")
first_node = code_parsed[0][0]
f.write("\t\"Entry Point\" -> \"" + str(first_node) + "\";\n")

# Graph content
for i in nodes:
    # f.write("\t" + i + " [ label = \"" + i + "\" ];\n")
    f.write("\t\"" + i + "\" [label = \"" + str(graph.node[i]['label']) + "\n" + str("0000" + str(i)) + "\"];\n")
    neigh = list(graph.neighbors(i))
    for j in range(len(neigh)):
        f.write("\t\"" + str(i) + "\" -> \"" + neigh[j] + "\" [label = \"" + str(graph.edges[str(i), str(neigh[j])]['label']) + "\"] ;\n")

#  Exit node
f.write("\t\"Exit\";\n")

if l_instr != -1:
    f.write("\t\"" + str(l_addr) + "\" -> \"Exit\";\n")
else:
    last_node = code_parsed[len(code_parsed) - 1][0]
    f.write("\t\"" + str(last_node) + "\" -> \"Exit\";\n")
f.write("}")
f.close()

print("Generating output file CFG.dot..")
os.system("dot -Tps CFG.dot -o CFG.pdf")
