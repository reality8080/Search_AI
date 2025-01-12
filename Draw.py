import matplotlib.pyplot as plt
import networkx as nx
import time
def visualize_search(order,title,G,pos):
    try:
        plt.figure()
        plt.title(title)
        for i, node in enumerate(order,start=1):
            plt.clf()
            plt.title(title)
            nx.draw(G,pos,with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
            plt.draw()
            plt.pause(1)
        plt.show()
        time.sleep(1)
    except ValueError:
        print(ValueError)