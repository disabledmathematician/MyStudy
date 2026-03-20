
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt

def Plot():
    plt.figure(0, dpi=150, figsize=[24, 12])
    G = nx.Graph()
    i, j, k, l = 1, 2, 3, 4
    for n in range(0, 8 - 3, 1):
    	print(n, n + i, n + j, n + k, n + l)
    	print("Connecting {} to {}, {}, {}, and {}".format(n, n + i, n + j, n + k, n + l))
    	G.add_edge(n, n + i, label="Fa")
    	G.add_edge(n, n + j, label="Bi")
    	G.add_edge(n, n + k, label="Jiao")
    	G.add_edge(n, n + l, label="Lee")
    	i += 3
    	j += 3
    	k += 3
    	l += 3
    edge_labels = nx.get_edge_attributes(G, "label")
    pos = nx.spring_layout(G, seed=5)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, width=0.5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#    plt.show()
    plt.savefig("WuHsing-8.png")
def CharlesTruscott():
    Plot()
    
CharlesTruscott()

