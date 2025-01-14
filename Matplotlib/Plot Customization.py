#Học matplotlib python
#https://www.youtube.com/watch?v=OZOOLe2imFo

import matplotlib.pyplot as plt
import numpy as np

#Dữ liệu
years=[2014 + X for X in range(8)]
income= np.random.normal(70,5,8)

#Vẽ đồ thị
income_ticks=list(range(50,81,5))
# Vẽ ticks cột y

plt.plot(years, income)
plt.title("Income of World (in USD)")
plt.xlabel("Year")# Label x
plt.ylabel("Yearly Income in USD")# Label y

plt.yticks(income_ticks,[f"{x}k USD" for x in income_ticks])

#Hiển thị
# plt.legend()
plt.grid()
plt.show()
