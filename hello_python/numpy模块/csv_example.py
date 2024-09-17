import csv
import random

with open("data.csv", "w", encoding="utf-8") as f:
    csvfile = csv.writer(f)
    for i in range(100):
        csvfile.writerow([random.randint(0, 10000) for j in range(4)])
