import numpy as np

import matplotlib.pyplot as plt

A=np.random.normal(90, 20,22)
B=np.random.normal(100, 30,22)
C=np.random.normal(110, 50,20)

plt.plot(A, label='A')
plt.plot(B, label='B')
plt.plot(C, label='C')

plt.grid()
plt.legend(loc='best')
#   Thông qua loc trong legend thì sẽ có thể điều chỉnh vị trí
#'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
plt.show()

# Chỉ nạp Y--> X sẽ tạo tự động theo size trong Y(số lượng phần tử của Y - 1 )