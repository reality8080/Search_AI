import matplotlib.pyplot as plt
import networkx as nx
import time

def visualize_search(order,edges ,title,G,pos):
    try:
        plt.figure()
        plt.title(title)
        for i, node in enumerate(order,start=1):
            plt.clf()
            plt.title(title)
            
            print(order)
            
            # Tô màu cạnh được duyệt
            edge_colors=[]
            for edge in G.edges():
                if edge in edges[:i] or (edge[1],edge[0]) in edges[:i]:
                    edge_colors.append('yellow')
                else:
                    edge_colors.append('black')
                print(edges)
            # Nếu muốn tô các 2 nút khác nhau bằng 2 màu khác nhau có thể thử enumerate
            nx.draw(G,pos,with_labels=True,
                    node_color=['r' if n == node else 'g' for n in G.nodes()],
                    edge_color=edge_colors,
                    )
            # plt.savefig('search_result/search_result_{}.png'.format(i))
            plt.draw()
            plt.pause(3)
        plt.show()
        time.sleep(3)
    except ValueError:
        print(ValueError)
            