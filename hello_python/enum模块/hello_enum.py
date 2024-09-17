from enum import IntEnum

class StudentEnum(IntEnum):
    Name, Age, Gender, Email = range(4)
   
from faker import Faker
import random

fake = Faker(locale="zh_CN")
student_informations = [(fake.name(), random.randint(16, 25), random.choice(["男", "女"]), fake.email()) for i in range(10)]
"""
student tuple:
    name 
    age
    gender
    email
"""    
for student_information in student_informations:
    print("name", student_information[StudentEnum.Name], "age", student_information[StudentEnum.Age], "gender", student_information[StudentEnum.Gender], "email", student_information[StudentEnum.Email])
    
