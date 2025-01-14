import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection="3d")
# Du lieu 1
# x=np.random.random(100)
# y=np.random.random(100)
# z=np.random.random(100)
# ax.scatter(x,y,z)
# ax.grid()
# Du lieu 2
# x=np.arange(0,100,0.01)
# y=np.sin(x)
# z=np.cos(x)
# ax.plot(x,y,z)

x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
Z=np.sin(X)*np.cos(Y)
ax.plot_surface(X, Y, Z,cmap='Spectral')

ax.view_init(azim=0,elev=90)

plt.grid()
plt.show()