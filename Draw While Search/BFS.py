import queue
import networkx as nx
import matplotlib.pyplot as plt

def order_BFS(graph, start_node):
    Queue=queue.Queue()
    visited=set()
    Queue.put(start_node)   #Thêm vào hàng đợi giá trị đầu tiên

    ordered=[]
    list_edge=[]
    # Bắt đầu vòng lặp
    
    # Hàng đợi rỗng thì = True
    while not Queue.empty():
        # Lấy giá trị đầu tiên ra khỏi hàng đợi
        u=Queue.get()
        # Nếu chưa được thăm.
        if u not in visited:
            visited.add(u)   #Thêm vào tập hợp đã thăm
            # Lấy giá trị của các đỉnh v liền kề u
            ordered.append(u)
            for v in graph[u]:
                if(v not in visited):
                    Queue.put(v)   #Đẩy vào hàng đợi
                    list_edge.append((u,v)) # Đẩy cạnh vào danh sách
                    # Kiểm tra danh sách xem cạnh có đỉnh đã đánh dấu hay chưa
                    for i in list_edge:
                        if i[0]!=u and i[1]==v:
                            list_edge.remove((u,v))
                            break
    # list_edge.insert(0,(start_node,start_node))
    return ordered, list_edge

if __name__ == "__main__":
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
    # Không thể để visited làm nơi chứa các đỉnh đã thăm, thiếu số 1.
    resultNodes,resultEdges=order_BFS(G,'1')
    print(resultNodes,resultEdges, sep="\n")
    # Đỉnh chưa vào hàng đợi sẽ có màu đỏ
    # Đỉnh được đưa vào hàng đợi sẽ có màu xanh lục
    # Đỉnh đang được xử lí xong sẽ có màu vàng
    # Đỉnh đã được xử lí xong sẽ có đen