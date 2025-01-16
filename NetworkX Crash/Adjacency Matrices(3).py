import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#Cách 1
# edge_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,4),(4,5),(5,6),(6,2)]
# G=nx.Graph()
# G.add_edges_from(edge_list)
# print(nx.adjacency_matrix(G))

# nx.draw_spring(G,with_labels=True)
# plt.show()

#Cách 2
a=np.array([[1,1,1],[1,0,0,],[0,0,1]])# Phải là ma trận vuông
A=nx.from_numpy_array(a)
nx.draw_spring(A,with_labels=True)
plt.show()