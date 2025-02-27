# Tìm kiếm theo chiều rộng là đi qua các đỉnh, gần với đỉnh ban đầu nhất, nếu không phải đỉnh cần tìm
# -->ghi giá trị của đỉnh vào hàng đợi
#Tiếp tục dựa trên hàng đợi và truy cập đến các đỉnh tiếp theo và lặp lại chương trình
#Tùy thuộc vào hình dạng đồ thì sẽ có từng cách tiếp cận khác nhau.
# Giả sử ta dùng ma trận toán học dòng, cột để biểu diễn đồ thị giữa 5 thành phố
# ---A=[
#           [0,0,0,0,0],
#           [0,0,0,0,0],
#           [0,0,0,0,0],
#           [0,0,0,0,0],
# ]
#   0 1 2 3 4
# 0 0 0 0 0 0 
# 1 0 0 0 0 0 
# 2 0 0 0 0 0 
# 3 0 0 0 0 0 
# 4 0 0 0 0 0 
# import numpy as np
# from collections import deque

# def Nhap(n:int ):
#     max=np.iinfo(np.int32).max
#     matrix=np.full((n,n), max, dtype=np.int32)
#     for i in range(n**2):   #full ma trận 2 chiềuchiều
#         a=input(f"{i+1}. Nhap A tu 0 den {n-1}: ")
#         b=input(f"{i+1}. Nhap B tu 0 den {n-1}: ")
#         try:
#             if not a or not b:  #Kiểm tra giá trị có rỗng
#                 break
            
#             a=int(a)
#             b=int(b)
#             if (0<=a<n) and (0<=b<n):
#                 matrix[a,b]=1
#             else: 
#                 print(a, b,"Khong hop le")
                
#         except ValueError:
#             print(ValueError)

#     # print(matrix)
#     return matrix
    
# def BFS(matrix:np.ndarray, n:int):
#     queue=deque()
#     x=int(input())
#     queue.appendleft(x)
#     while(not queue):
#         i=queue.pop()
#         for j in range (n):
#             if matrix[i,j]==1:
#                 queue.appendleft(j)
        
    
    

# if __name__ == "__main__":
#     # row=int(input())
#     # col=int(input())
#     # for i in range(row):
#     #     list1=[]
#     #     for j in range(col):
#     #         a=int(input())
#     #         # if a==0 or a==1 :
#     #         list1.append(a)
#     #     matrix.append(list1)
#     # matrix=np.array(matrix)
#     # # print(matrix)
#     n=int(input(f"Nhap N: "))
#     matrix=Nhap(n)
#     print(matrix)


#https://www.youtube.com/watch?v=7XVTnCrWDPY
import queue
import networkx as nx
import matplotlib.pyplot as plt


def order_bfs(graph, start_node):
    visited=set()                               #Tập hợp các đỉnh Đã thăm(Khong phải thứ tự thăm, tránh taoh vòng lặp)
    q=queue.Queue()                             #Hàng đợi
    q.put(start_node)                           #Đưa node vào hàng đợi
    order=[]                                    #Danh sách thứ tự thăm các đỉnh, có chức năng gần giống visited nhưng không phải set
    edges = []                                  # Danh sách các cạnh đã duyệt
    
    while not q.empty():                        #Nếu hàng đợi trống
        vertex=q.get()                          #Lấy đỉnh dầu tiên theo FIFO 
        if vertex not in visited:               #Nếu lần đầu đến thăm, chưa được thăm
            order.append(vertex)                #Thêm vào danh sách các đỉnh đã thăm 
            visited.add(vertex)                 #Thêm đã thăm
            for node in graph[vertex]:          # Lấy dữ liệu graph, graph[vertex] là các đỉnh liền kề của đỉnh đã chọn
                if node not in visited:         #Nếu đỉnh liền kề chưa được thăm
                    q.put(node)                 #Đỉnh liền kề đó sẽ được đưa vào hàng đợi
                    edges.append((vertex, node))# Lưu lại cạnh được duyệt
                    for v in edges[:len(edges)-1]:
                        if v[0]!=vertex and v[1]==node:
                            edges.remove((vertex,node))
    edges.insert(0,(f'start_node',f'start_node'))                
    return order,edges                                #Trả về danh sách thứ tự thăm và danh sách cạnh

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
    pos=nx.spring_layout(G)
    order,edges=order_bfs(G,start_node='1')
    print(order,edges,sep='\n')