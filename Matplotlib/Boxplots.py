#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

# #Dữ liệu 1
# heights=np.random.normal(loc=100,scale=8 ,size=300)
# #Vẽ đồ thị
# plt.boxplot(heights)
# #Hiển thị
# plt.legend()
# # plt.grid()
# plt.show()

# Dữ liệu 2
first=np.linspace(0,10,25)                      #Mảng 25 giá trị 0 đến 10
second=np.linspace(10,200,25)                   #Mảng 25 giá trị 10 đến 200
third=np.linspace(200,210,25)                   #Mảng 25 giá trị 200 đến 210
fourth=np.linspace(210,230,25)                  #Mảng 25 giá trị 210 đến 230

data=np.concatenate((first,second,third,fourth))
 
plt.boxplot(data)
plt.legend()
plt.grid()
plt.show()