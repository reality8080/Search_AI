import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="tip", hue="sex", palette="YlGnBu",dodge=True)

sns.stripplot(data=tips, x="day", y="tip", hue="sex", palette="YlGnBu",dodge=True)

plt.legend("left")
plt.grid()
plt.show()