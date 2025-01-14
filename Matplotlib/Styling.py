import numpy as np
import matplotlib.pyplot as plt

import matplotlib.style as Style

Style.use("")

Label=["Python","C++","C#","Java","Go","MongGoDB"]

amount=np.random.random(6)*100
explodes=np.random.normal(0.2,0.01,6)
plt.pie(amount, labels=Label,explode=explodes, autopct="%.3f%%",
        pctdistance=0.55, startangle=0)

# plt.legend(loc='upper right')
plt.grid()
plt.show()
# https://matplotlib.org/stable/gallery/index.html
# https://matplotlib.org/stable/api/index.html
# https://matplotlib.org/stable/tutorials/index.html