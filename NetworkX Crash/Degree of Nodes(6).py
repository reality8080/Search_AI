import networkx as nx
import matplotlib.pyplot as plt

edge_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,4),(4,5),(5,6),(6,2)]

G=nx.DiGraph()

G.add_edges_from(edge_list)

print(dict(G.degree)[1])
#In số cạnh quanh node, Graph
print(dict(G.in_degree)[1])
#In số vector quanh node, đi vào, DiGraph
print(dict(G.out_degree)[1])
#In số vector quanh node, đi ra, DiGraph

nx.draw_spring(G,with_labels=True)
plt.show()