import csv
import os
import random

base_file_path = r"D:\bilibili"
if not os.path.exists(base_file_path):
    os.mkdir(base_file_path)
with open("./name.csv", "w", encoding="utf-8") as f:
    csvfile = csv.writer(f)
    for i in range(100):
        file_path = os.path.join(base_file_path, f"name_{i}.csv")
        csvfile.writerow([f"name_{i}.csv"])
        if random.random() >= 0.5:
            f = open(file_path, "w")
            f.close()
