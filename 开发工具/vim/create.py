import faker
import csv
import random

fake = faker.Faker(locale="zh_CN")
with open("example.csv", "w", encoding="utf-8") as f:
    csvfile = csv.writer(f)
    for i in range(100):
       csvfile.writerow([fake.name(), random.randint(0, 100)]) 