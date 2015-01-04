__author__ = 'zog'

from project_euler_libs import *
import networkx as nx
import matplotlib.pyplot as plt
import math as m

total_nodes = 12
index = total_nodes + 1
total = 0
G = nx.grid_graph([index,index])

#H=nx.path_graph(11)
#G.add_nodes_from(H)
#G.add_edge((0,0),(2,2))



print "nodes: ",G.nodes()
print "edges: ",G.edges()
#all_paths = nx.all_simple_paths(G, source=(0,0), target=(20,20), cutoff=0)
#for path in all_paths:
    #print "path: ",path
#    total = total + 1


for nodes in range(total_nodes):
    shortest_total = 0
    target_node = (nodes,nodes)
    print "target_node:",target_node
    shortest_paths = nx.all_shortest_paths(G, (0,0), target_node, weight=0)
    #print "type: ",type(shortest_paths)
    for path in shortest_paths:
        #print "path: ",path
        shortest_total = shortest_total + 1
        if (shortest_total % 100000 == 0):
            print "shortest_total: ",shortest_total

    #print "total_paths: ",total
    print "nodes: ",nodes,"total_shortest_paths: ",shortest_total
    paths_guess = m.factorial(2*nodes)/((m.factorial(nodes))**2)
    print "paths_guess: ",paths_guess

nodes = 20
paths_guess = m.factorial(2*nodes)/((m.factorial(nodes))**2)
print "final_paths_guess: ", paths_guess
#nx.draw(G)
#plt.show()