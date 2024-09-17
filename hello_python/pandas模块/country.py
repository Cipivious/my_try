import random
import csv

# 定义六七个国家的名字
countries = ["China", "USA", "India", "Brazil", "Russia", "Australia", "Japan"]

# 打开或创建一个 CSV 文件
with open("countries_combinations.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # 生成 10 个随机组合，写入 CSV 文件
    for _ in range(100):
        # 随机取 2 到 4 个国家
        selected_countries = random.sample(countries, random.randint(2, 4))
        # 将国家名称拼接成一个字符串
        combined_countries = ",".join(selected_countries)
        # 将字符串写入 CSV 文件
        writer.writerow([combined_countries])

print("CSV 文件生成成功！")
