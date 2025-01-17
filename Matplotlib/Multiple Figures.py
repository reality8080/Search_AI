import numpy as np
import matplotlib.pyplot as plt


x1,y1=np.random.random(100), np.random.random(100)
x2,y2=np.arange(100), np.random.random(100)
plt.figure(1)
plt.scatter(x1,y1)

plt.figure(2)
plt.plot(x2,y2)

plt.show()
# Nhiều đồ thị