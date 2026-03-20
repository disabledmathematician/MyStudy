"""
 (Can the true walk through a financial optimisation tree become a spanning tree out of all other hypothetical walks?)
 Charles Thomas Wallace Truscott Watters. 127 Broken Head Rd, Suffolk Park, NSW 2481
 
"""
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt

def Plot():
    plt.figure(0, dpi=150, figsize=[12, 7])
    count = 4
    L = [x for x in range(1, 4 **  count + 4, 1)]
    while count <= 4:
        i, j = 1, 2
        k, l = 3, 4
        x = 0
        G = nx.Graph()
#        print(len(L))
        while (x < (math.log(len(L), 4))):
        	print("x: {} attaches to {}, {}, {}, {}".format(x, i, j, k, l))
        	G.add_edge(L[x], L[x + i], label="Fa")
        	G.add_edge(L[x], L[x + j], label="Bi")
        	G.add_edge(L[x], L[x + k], label="Jiao")
        	G.add_edge(L[x], L[x + l], label="Lee")
        	i, j, k, l = i + 4, j + 4, k + 4, l + 4
        	x += 1
#            x += l
#            i += 1
#            j += 1
#            k += 1
#            l += 1
        count += 1
    edge_labels = nx.get_edge_attributes(G, "label")
    pos = nx.spring_layout(G, seed=5)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, width=0.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.savefig("WuHsing.png")
def CharlesTruscott():
    Plot()
    
CharlesTruscott()

