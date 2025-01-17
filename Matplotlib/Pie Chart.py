#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

#Dữ liệu
Label=["Python","C++","C#","Java","Go","MongGoDB"]
# Tạo nhãn
amount=np.random.random(6)*100
# Tạo giá trị random 6 giá trị, trong khoảng 0 đến 100
explodes=np.random.normal(0.2,0.01,6)
# Random 6 giá trị trong khoảng 0.2 với độ lệch chuẩn 0.1
#Vẽ đồ thị
plt.pie(amount, labels=Label,explode=explodes, autopct="%.3f%%",
        pctdistance=0.55, startangle=0)
# Tham số pctdistance trong hàm plt.pie() 
    # xác định khoảng cách từ tâm của biểu đồ 
    # tròn đến vị trí hiển thị phần trăm (percentage) 
    # của mỗi phần.
# autopct: viết số % trong pie
# startangle: là vị trí bắt đầu, =0 thì sẽ bắt đầu bên phải
#Hiển thị
# plt.legend()
plt.grid()
plt.show()