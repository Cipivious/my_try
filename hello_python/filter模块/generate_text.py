import faker

fake = faker.Faker()

with open("text.txt", "w", encoding="utf=8") as f:
    for _ in range(10):
        f.write(fake.text())
        f.write("\n")