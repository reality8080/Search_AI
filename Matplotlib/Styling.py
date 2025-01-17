import numpy as np
import matplotlib.pyplot as plt

import matplotlib.style as Style

Style.use("ggplot")
# print(plt.style.available)
# Có thể xem Style có thể dùng những loại nào.
# Các loại phổ biến:
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery',
# '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
# 'fast', 'fivethirtyeight', 'ggplot', 'grayscale',
# 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 
# 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette',
# 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 
# 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
# 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

Label=["Python","C++","C#","Java","Go","MongGoDB"]

amount=np.random.random(6)*100
explodes=np.random.normal(0.2,0.01,6)
plt.pie(amount, labels=Label,explode=explodes, autopct="%.3f%%",
        pctdistance=0.55, startangle=0)

# plt.legend(loc='upper right')
plt.grid()

plt.show()
# https://matplotlib.org/stable/gallery/index.html
# https://matplotlib.org/stable/gallery/index.html
# https://matplotlib.org/stable/tutorials/index.html