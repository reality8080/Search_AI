import networkx as nx
import matplotlib.pyplot as plt
#Cách 1
edge_list1=[(1,2),(2,3),(1,3),(1,4),(2,5)]
G=nx.from_edgelist(edgelist=edge_list1)
# nx.draw_spring(G,with_labels=True)
#Cách 2

edge_list2=[(1,2),(2,3),(1,3),(1,4),(2,5)]
E=nx.Graph()
E.add_edges_from(edge_list2)
nx.draw_spring(E,with_labels=True)
plt.show()