import networkx as nx
import matplotlib.pyplot as plt

#Hướng dẫn các cách thêm cạnh
A=nx.Graph()
# Đồ thị vô hướng
B= nx.DiGraph()
# Đồ thị có hướng
C=nx.MultiGraph()
# Đa đồ thị, đồ thị một nút có nhiều cạnh
D=nx.MultiDiGraph()
# Đa đồ thị, có hướng
A.add_edge(1,2,weight=0.1)
A.add_edge(1,3)
A.add_edge(1,4)
A.add_edge(2,3)
A.add_edge(2,4)
A.add_edge(2,2,weight=0.1)
A.add_edge(3,2)
A.add_edge(4,3)
A.add_node("100")
A.add_node(print)
nx.draw_spring(A, with_labels=True)


plt.show()
#weight, gắn trọng số cho cạnh