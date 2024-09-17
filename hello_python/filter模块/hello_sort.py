import faker
import random
fake = faker.Faker(locale="zh_CN")

# student_informations = [{"name": fake.name(), "age": random.randint(12, 18), "score": random.randint(0, 99)} for i in range(10)]

# sorted_student_informations = sorted(student_informations, key= lambda item: item["age"] * 0.6 + item["score"] * 0.4, reverse=True)

# print(student_informations)
# print(sorted_student_informations)

student_informations = {fake.name(): random.randint(0, 100) for _ in range(10)}
sorted_student_informations = sorted(student_informations.items(), key=lambda item: item[1])
print(student_informations)
print(sorted_student_informations)
