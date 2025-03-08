import networkx as nx
import matplotlib.pyplot as plt
import time

def draw(graph, nodes, edges,parent,found, path=[] ):
    
    nodeColor={node:'Gray' for node in graph.nodes}
    edgeColor=[]

    for edge in graph.edges():
        if edge in edges or (edge[1],edge[0]) in edges:
            edgeColor.append('yellow')
        else:
            edgeColor.append('black')

    for node in nodes:
            if(parent[node] is None):
                nodeColor[node]='red'
            else:
                nodeColor[parent[node]]='red'
                nodeColor[node]='blue'
                # edgeColor.append('yellow')
    if found:
        for node in graph.nodes():
            if node in path:
                nodeColor[node] = 'yellow'
            else:
                nodeColor[node] = 'gray'

    nodeColorList=[nodeColor[node] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True,
            node_color=nodeColorList,
            edge_color=edgeColor,
            node_size=800,
            font_size=14,
            width=2)
                
    plt.draw()
    plt.pause(1.5)
            

def DFS(graph, startNode, endNode, title):
    try:
        visited_nodes = list()
        stack = [startNode]
        parent={startNode:None}
        edges=[]
        found=False
        path=[]

        while stack:
            u = stack.pop()

            if u not in visited_nodes:
                visited_nodes.append(u)
                
                # if(parent[u]!=np.nan):
                #     parent[u]=before
                #     edges.append((parent[u], u))
                
                # Kiểm tra xem u có trong graph không để tránh KeyError
                if(parent[u] is not None):
                    edges.append((parent[u],u))

                for v in sorted(graph[u], reverse=True):
                    if v not in parent:
                        stack.append(v)
                        parent[v]=u
                plt.clf()
                plt.title(f"DFS: {visited_nodes}")
                draw(graph, visited_nodes,edges, parent,found, path)
                # before=u
                if(u==endNode):
                    found=True
                    break
        if(found):
            path=[endNode]
            cur=endNode
            while cur!=startNode:
                cur=parent[cur]
                path.append(cur)
            path.reverse()
            plt.clf()
            plt.title(title)
            draw(graph, visited_nodes,edges, parent,found,path)       
        time.sleep(2)
        plt.show()
    except ValueError as e:
        print(e)
    

if __name__ =='__main__':
    # graph={
    #     '1': ['2', '4', '8'],
    #     '2': ['1', '3', '7'],
    #     '3': ['2', '4', '6'],
    #     '4': ['1', '3', '5'],
    #     '5': ['4', '7', '8'],
    #     '6': ['3'],
    #     '7': ['2', '5', '8'],
    #     '8': ['1', '5', '7']
    # }


    G = nx.Graph()  # Tạo một đồ thị vô hướng
    # for node, neighbors in graph.items():
    #     for neighbor in neighbors:
    #         G.add_edge(node, neighbor)
    G.add_edges_from([
        ('1','2'),('1','4'),('1','8'),('2','3'),('2','7'),('4','3'),('4','5'),('3','6'),
        ('8','7'),('8','5'),('7','5')
    ])
    
    pos=nx.spring_layout(G)
    DFS(G,'1','8','DFS')