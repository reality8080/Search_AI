# Khai báo hàng đợi như list
q=[]
# Chèn giá trị
q.insert(0,1)
q.insert(1,2)# Nếu chèn một giá trị ở vị trí khác thì sẽ không đẩy các giá trị phía trái, mà đặt giá trị đó ở phía trái 
q.insert(0,3)
q.insert(0,4)
q.insert(0,5)
q.insert(0,6)
q.insert(0,7)
q.insert(0,8)# cùng đặt ở một vị trí thì đẩy vị trí trước đó ra phía sau và chèn giá trị mới 
q.append(9)#Đặt 9 ở sau cùng
print(q)
print(q.pop())# Lấy giá trị đầu tiên bên trái
print(q)

# Tạo queue thông qua Deque
from collections import deque
q=deque()
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)
print(q)
print(q.pop())
print(q)