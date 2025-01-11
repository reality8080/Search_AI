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
    # row=int(input())
    # col=int(input())
    # for i in range(row):
    #     list1=[]
    #     for j in range(col):
    #         a=int(input())
    #         # if a==0 or a==1 :
    #         list1.append(a)
    #     matrix.append(list1)
    # matrix=np.array(matrix)
    # # print(matrix)
    n=int(input(f"Nhap N: "))
    matrix=np.zeros([n,n], dtype=int)
    for i in range(n**2):   #full ma trận 2 chiềuchiều
        a=input(f"Nhap A tu 0 den {n-1}: ")
        b=input(f"Nhap B tu 0 den {n-1}: ")
        try:
            if not a or not b:  #Kiểm tra giá trị có rỗng
                break
            
            a=int(a)
            b=int(b)
            if (0<=a<n) and (0<=b<n):
                matrix[a,b]=1
            else: 
                print(a, b,"Khong hop le")
                
        except ValueError:
            print(ValueError)
    # # print(matrix)
    # x1=int(input())
    # x2=int(input())
    print(matrix)
    