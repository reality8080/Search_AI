import matplotlib.pyplot as plt
import networkx as nx
import time

def visualize_search(order,edges ,title,G,pos):
    try:
        plt.figure(figsize=(8,6))
        plt.title(title)
        
        visited_edges=set()
        
        for i, node in enumerate(order,start=1):
            plt.clf()
            plt.title(f"{title} - Step{i}/{len(order)}") 
            
            if i<=len(edges):
                visited_edges.add(edges[i-1])           
            # Tô màu cạnh được duyệt
            edge_colors=[]
            # list_edges_visited=list()
            for edge in G.edges():
                if edge in edges[:i] or (edge[1],edge[0]) in edges[:i]:
                    edge_colors.append('yellow')
                else:
                    edge_colors.append('black')     
                # list_edges_visited.append(edge)
            
            # Tô node
            # Tô màu các node ban đầu bằng dict
            node_colors={node:'green' for node in G.nodes()}
            
            # Tô màu các node sẽ duyệt
            for edge in edges[:i]: # duyệt các cạnh đến cạnh i-1
                # Tô node gốc
                node_colors[edge[0]]='red'
                # Tô node đỉnh
                node_colors[edge[1]]='yellow'
            # chuyển từ dict sang list
            node_colors_list=[node_colors[node] for node in G.nodes()]
            
            # Nếu muốn tô các 2 nút khác nhau bằng 2 màu khác nhau có thể thử enumerate
            nx.draw(G,pos,with_labels=True,
                    node_color=node_colors_list,
                    edge_color=edge_colors,
                    node_size=800,
                    font_size=14,
                    width=2,
                    )
            # plt.savefig('search_result/search_result_{}.png'.format(i))
            plt.draw()
            plt.pause(1.5)
        plt.show()
        time.sleep(3)
    except ValueError:
        print(ValueError)
            