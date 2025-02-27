import networkx as nx

import matplotlib.pyplot as plt

def DFS(graph,startNode):
    visited_nodes=list()
    stack=[startNode]
    edges=[]
    
    while stack:
        u=stack.pop()
        if u not in visited_nodes:
            visited_nodes.append(u)
            for v in reversed(sorted(graph[u])):
                if v not in visited_nodes:
                    stack.append(v)
                    edges.append((u,v))
    return visited_nodes,edges
if __name__ =='__main__':
    G=nx.Graph()
    
    G.add_edges_from([
        ('1','2'),('1','4'),('1','8'),('2','3'),('2','7'),('4','3'),('4','5'),('3','6'),
        ('8','7'),('8','5'),('7','5')
    ])
    
    pos=nx.spring_layout(G)
    visited,result=DFS(G,'1')
    print(visited,result,sep='\n')