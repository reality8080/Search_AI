#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

#Dữ liệu
ages=np.random.normal(loc=30,scale=1.5,size=1000)
# loc: là giá trị trung bình
#scale: là giá trị lệch chuẩn
#size: số lượng mẩu thử
#Vẽ đồ thị
# plt.bar(X_data,Y_Data,color="#0f0")
# plt.hist(ages, bins=[ages.min(),28,32,ages.max()])
plt.hist(ages, bins=50, cumulative=True)

#Hiển thị
plt.legend()
plt.grid()
plt.show()
