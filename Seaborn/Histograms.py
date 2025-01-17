import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
# print(tips.head())
# sns.histplot(data="tips", x="total_bill")
# sns.histplot(data=tips,x="total_bill", kde=True)
# Hoặc
sns.histplot(data=tips["total_bill"], kde=True, bins="auto")
plt.show()