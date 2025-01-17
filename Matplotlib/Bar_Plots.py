#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

#Dữ liệu
X_data=["C++","C#", "Python","Java","Go"]
# Y_Data=[100,100,40,60,10]
Y_Data=np.random.random(5)* 100

#Vẽ đồ thị

# plt.bar(X_data,Y_Data,color="#0f0")
plt.bar(X_data,Y_Data,color="#0f0", align="edge", width=0.5,edgecolor="blue",lw=3)

#Hiển thị
plt.legend()
plt.grid()
plt.show()
#Nhặt banh:
#Hiệu quả: Nhặt nhanh, vị trí nhặt ở đâu, số lượng
# Môi trường: Banh có trên sân, sân banh
# Các bộ phận: Bộ phận lấy banh, máy hút, bánh xe, rổ chứa
# Cảm biến: camera, 
# 
# 
# Vẽ cột dữ liệu
# 
# #