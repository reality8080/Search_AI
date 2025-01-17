import numpy as np
import matplotlib.pyplot as plt

x=np.arange(100)

fig, axs=plt.subplots(2,2)

# Chia làm 4 đồ thị(2*2)

axs[0,0].plot(x,np.sin(x))

axs[0,1].plot(x,np.cos(x))

axs[1,0].plot(x,np.tan(x))

axs[1,1].plot(x,np.log(x))

plt.grid()
plt.show()
# Phân hình để chứa nhiều đồ thị