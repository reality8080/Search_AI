#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

X_data=np.random.random(1000)*100
Y_data=np.random.random(1000)*100
plt.scatter(X_data,Y_data,color='#f0f', s=100, marker="*", alpha=0.5)

plt.legend()
plt.grid()
plt.show()
#  Đồ thị tập trung