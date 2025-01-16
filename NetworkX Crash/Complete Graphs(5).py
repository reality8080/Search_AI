import networkx as nx
import matplotlib.pyplot as plt

G=nx.complete_graph(12)

# nx.draw_spring(G,with_labels=True)
# nx.draw_planar(G,with_labels=True)
#draw_planar: complete_graph phải <=4
# nx.draw_random(G,with_labels=True)
nx.draw_kamada_kawai(G,with_labels=True)
# ..., còn rất nhiều cách vẽ.
plt.show()