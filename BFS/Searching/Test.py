import networkx as nx
import queue
import matplotlib.pyplot as plt
import time

def visualizing(Graph,edges,step,visited):
    edges_colors=[]
    for edge in Graph.edges():
        if edge in edges[:step] or (edge[1],edge[0]) in edges[:step]:
            edges_colors.append('blue')
        else:
            edges_colors.append('black')
                # Tô node chưa thăm, đã thăm
    node_colors={node:'green' for node in Graph.nodes}
    for edge in edges[:step]:
        if edge[0] not in visited or edge[1] not in visited:
            if edge[0] and len(edge)>0:
                node_colors[edge[0]]='red'
            if edge[1] and len(edge)>0:
                node_colors[edge[1]]='blue'
        else:
            node_colors[edge[0]]='gray'
            node_colors[edge[1]]='gray'
    node_colors_list=[node_colors[node] for node in Graph.nodes()]
    nx.draw(Graph, pos, with_labels=True,
            node_color=node_colors_list,
            edge_color=edges_colors,
            node_size=800,
            font_size=14,
            width=2)
                
    plt.draw()
    plt.pause(1.5)
    

def BFS(Graph,start, title, pos):
    try:
        # Ve do thi
        plt.figure(figsize=(8,6))
        #Du lieu node
        visited=set()
        q=queue.Queue()
        # orders=[]
        edges=[]
        step=0
        
        q.put(start)
        # edges.append((f'{start}',f'{start}'))
        
        while not q.empty():
            u=q.get()
            if u not in visited:
                # orders.append(u)
                visited.add(u)
                step += 1
                # Tô màu
                plt.clf()
                plt.title(title)
                # Tô màu cạnh
                
                for v in Graph[u]:
                    if v not in visited:
                        q.put(v)
                        edges.append((u,v))
                        for i in edges[:len(edges)-1]:
                            if(i[0]!=u and i[1]==v):
                                edges.remove((u,v))
                visualizing(Graph,edges,step,visited)
        plt.legend()
        time.sleep(2)
        plt.show()
    except ValueError:
        print(ValueError)

if __name__=='__main__':
    G=nx.Graph()
    
    G.add_edges_from([
        ('1','2'),('1','4'),('1','8'),('2','3'),('2','7'),('4','3'),('4','5'),('3','6'),
        ('8','7'),('8','5'),('7','5')
    ])
    
    pos=nx.circular_layout(G)
    start_node='1'
    BFS(G,start_node,'BFS',pos)

