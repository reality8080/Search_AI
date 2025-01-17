#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

X_data=[2006+X for X in range(14)]
Y_data=np.random.random(14)*100

# plt.plot(X_data,Y_data, color='red', lw=5, linestyle="--")
plt.plot(X_data,Y_data,"r--",lw=4)

plt.legend()

plt.grid()
plt.show()
# Đồ thị đường