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
import numpy as np

if __name__ == "__main__":
    matrix=[]
    row=int(input())
    col=int(input())
    for i in range(row):
        list1=[]
        for j in range(col):
            a=int(input())
            if a==0 or a==1 :
                list1.append(a)
        matrix.append(list1)
    matrix=np.array(matrix)
    print(matrix)
    