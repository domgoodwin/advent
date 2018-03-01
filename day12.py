f = open('inputs/day12.txt', 'r')

import networkx as nx

graph = nx.Graph()


for line in f:
    #print(line)
    node, progs = line.split(" <-> ")
    for prog in progs.split(", "):
        graph.add_edge(node, prog.strip())


print('Part 1:', len(nx.node_connected_component(graph, '0')))
print('Part 2:', nx.number_connected_components(graph))
