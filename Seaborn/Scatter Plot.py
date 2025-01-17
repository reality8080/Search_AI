import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset("tips")
sns.scatterplot(x="tip", y="total_bill", data=tips, hue="day", size="size", palette="flare")
# x,y: hệ trục tọa độ
# hue="day": là đánh giấu những chấm trong đồ thị
# size="size": là độ lớn của những chấm trong scatter.
# palette="YlGnBu" là chọn màu cho các chấm
# print(sns.color_palette())

plt.legend()
plt.grid()
plt.show()