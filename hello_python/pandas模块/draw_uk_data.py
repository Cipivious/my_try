import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 读取数据
df = pd.read_csv("./uk_data.csv")

# 将第一列的数据转换为列表
data = df.iloc[:, 0].tolist()
index = 0
for item in df:
    print(item)
    if index > 10:
        break
    index += 1
print(data)

# 计算最大值和最小值
max_value = max(data)
min_value = min(data)

# 计算宽度
width = (max_value - min_value) / 10
print(width)

# 计算箱的数量
bins = int((max_value - min_value) / width)
x_value = np.arange(0, 10000, width)
# 绘制直方图
plt.figure(figsize=(20, 8))
plt.hist(data, bins=bins, edgecolor="black")
plt.xticks(x_value)
plt.show()
