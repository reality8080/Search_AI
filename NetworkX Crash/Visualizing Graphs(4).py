import networkx as nx
import matplotlib.pyplot as plt

edge_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,4),(4,5),(5,6),(6,2)]
G=nx.Graph()
G.add_edges_from(edge_list)

# nx.draw_spring(G,with_labels=True)

# nx.draw_circular(G,with_labels=True)

# nx.draw_shell(G,with_labels=True)

# nx.draw_spectral(G,with_labels=True)

# nx.draw_random(G,with_labels=True)

# nx.draw_planar(G,with_labels=True)

nx.draw
plt.show()
