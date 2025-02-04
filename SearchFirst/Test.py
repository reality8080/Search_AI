#https://www.youtube.com/watch?v=7XVTnCrWDPY
import networkx as nx
import Draw
from Uninformed_Search import Breadth_First_Search
import matplotlib.pyplot as plt

if __name__ =='__main__':
    G=nx.Graph()
    G.add_edges_from([('1','2'),
                      ('1','4'),
                      ('1','8'),
                      ('2','3'),
                      ('2','7'),
                      ('4','3'),
                      ('4','5'),
                      ('3','6'),
                      ('8','7'),
                      ('8','5'),
                      ('7','5'),])
    pos=nx.spring_layout(G)
    order,edges=Breadth_First_Search.order_bfs(G,start_node='1')
    
    Draw.visualize_search(order=order, edges=edges,title='BFS Visualization',G=G,pos=pos)