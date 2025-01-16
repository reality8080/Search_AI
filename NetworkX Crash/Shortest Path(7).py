import matplotlib.pyplot as plt
import networkx as nx

edge_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,4),(4,5),(5,6),(6,2)]

# G=nx.DiGraph()
G=nx.Graph()

G.add_edges_from(edge_list)

print(nx.shortest_path(G,2,4))
# Đường đi ngắn nhất

nx.draw_spring(G,with_labels=True)
plt.show()