import matplotlib.pyplot as plt
import networkx as nx

G1=nx.complete_graph(5)
G2=nx.complete_graph(5)
G2=nx.relabel_nodes(G2,{0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"})
G_connector=nx.from_edgelist([(4,"X"),("A","X")])
G=nx.compose_all([G1,G2,G_connector])

print(list(nx.bridges(G)))

nx.draw_spring(G,with_labels=True)
plt.show()