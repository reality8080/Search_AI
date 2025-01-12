import networkx as nx
import Draw
from Uninformed_Search import Breadth_First_Search


if __name__ =='__main__':
    G=nx.Graph()
    G.add_edges_from([('1','2'),
                      ('2','3'),
                      ('3','4'),
                      ('4','1'),
                      ('1','5'),
                      ('2','6'),
                      ('3','7'),
                      ('4','8'),
                      ('5','6'),
                      ('6','8'),
                      ('8','5'),])
    pos=nx.spring_layout(G)
    Draw.visualize_search(Breadth_First_Search.order_bfs(G,start_node='1'),title='BFS Visualization',G=G,pos=pos)