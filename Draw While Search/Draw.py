import matplotlib.pyplot as plt
import networkx as nx
import time

def visualize_search(order,edges, title,G,pos):
    try:
        plt.figure()
        plt.title(title)
        for i, node in enumerate(order,start=1):
            plt.clf()
            plt.title(title)
            
            # Tô màu cạnh được duyệt
            
            # node_color=[]
            edges_colors=[]
            for j in G.edges():
                if j in edges[:i]:
                    edges_colors.append('yellow')
                else:
                    edges_colors.append('black')
            
            node_colors=['r' if i == node else 'g' for i in G.nodes()]
            nx.draw(G,pos,with_labels=True,
                    node_color=node_colors,
                    edge_color=edges_colors,
                    )

            plt.draw()
            plt.pause(3)
        plt.show()
        time.sleep(3)
    except ValueError:
        print(ValueError)   