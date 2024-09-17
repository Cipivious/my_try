from matplotlib import pyplot as plt
import random
import math
import time
from matplotlib import font_manager

font_prop = font_manager.FontProperties(fname=r"C:\Windows\Fonts\msjh.ttc")

y = []
x = []
num = 1
base_num = 1
x_label = []
other_y = []
for i in range(20):
    if i > 13:
        x.append(num)
    y.append(base_num)
    other_y.append(base_num * random.uniform(0.9, 1.1))
    x_label.append(f"12点{i+1}分")
    num = num * math.e
    base_num = base_num * math.e

plt.figure(figsize=(20, 8))
plt.yticks(x)
plt.xticks(
    ticks=range(len(x_label)), labels=x_label, rotation=270, fontproperties=font_prop
)
plt.xlabel("时间", fontproperties=font_prop)
plt.ylabel("强度", fontproperties=font_prop)
plt.grid()
plt.title("强度随温度的变化图", fontproperties=font_prop)
plt.plot(range(20), y, label="line1")
plt.scatter(range(20), other_y, label="line2")
plt.legend()
plt.show()
plt.close()
plt.figure(figsize=(20, 8))
plt.yticks(x)
plt.xticks(
    ticks=range(len(x_label)), labels=x_label, rotation=270, fontproperties=font_prop
)
plt.xlabel("时间", fontproperties=font_prop)
plt.ylabel("强度", fontproperties=font_prop)
plt.grid()
plt.title("强度随温度的变化图", fontproperties=font_prop)
bar_width = 0.2
plt.bar(range(20), y, label="line1", width=bar_width)
plt.bar([i + bar_width for i in range(20)], other_y, label="line2", width=bar_width)
plt.legend()
plt.show()
