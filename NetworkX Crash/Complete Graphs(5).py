import networkx as nx
import matplotlib.pyplot as plt

G=nx.complete_graph(8)

# nx.draw_spring(A,with_labels=True)
# plt.show()
nx.draw_planar(G,with_labels=True)
plt.show()