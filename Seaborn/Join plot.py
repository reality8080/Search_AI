import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.jointplot(data=tips, y="total_bill", x="tip", kind="kde",shade=True)
# Đồ thị thể hiện tần suất một cách trực quan
# ĐỒ thị chứa kiểu kind và các cột ngoài viền
# Có sáu kiểu có thể lựa: hex, kde, hist, reg, resid, scatter
plt.grid()
plt.show()