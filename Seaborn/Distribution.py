import seaborn as sns

import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.displot(data=tips, x="total_bill", kde=True)
plt.show()