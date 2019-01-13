# Using NetworkX as library for the creation of Graphs
import networkx as nx

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
        code.append(row.strip())
        while end_main == 0:
            row = f.readline()
            if row == "\n":  # Searching ending point (empity line)
                end_main = 1
                end_lecture = 1
            else:
                code.append(row.strip())  # Strip() removes the extra \n

# Closure of the file
f.close()

for i in code:
    print(i)
