import matplotlib.pyplot as plt
import networkx as nx

edge_list=[(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,4),(4,5),(5,6),(6,2)]

# G=nx.DiGraph()
G=nx.Graph()


G.add_edges_from(edge_list)


print(nx.degree_centrality(G))
# Tính toán tầm quan trọng của một đỉnh dựa trên 
# số lượng kết nối trực tiếp (bậc) của nó so với 
# tổng số đỉnh trong đồ thị trừ đi 1.
print(nx.closeness_centrality(G))
# Đo lường mức độ "gần gũi" của một đỉnh đến tất 
# cả các đỉnh khác trong đồ thị. Đỉnh càng gần 
# (ít bước di chuyển hơn) đến các đỉnh khác thì
# giá trị càng cao.
print(nx.eigenvector_centrality(G))
#  Đo lường tầm quan trọng của một đỉnh không chỉ 
# dựa vào số kết nối trực tiếp, mà còn dựa vào tầm
# quan trọng của các đỉnh mà nó kết nối. Đỉnh được 
# kết nối với các đỉnh "quan trọng" sẽ có giá trị 
# cao hơn.
print(nx.betweenness_centrality(G))
#  Đo lường tầm quan trọng của một đỉnh dựa trên số
# lượng đường đi ngắn nhất giữa các cặp đỉnh khác đi
# qua đỉnh đó. Đỉnh đóng vai trò "cầu nối" sẽ có giá
# trị cao hơn


nx.draw_spring(G,with_labels=True)
plt.show()


