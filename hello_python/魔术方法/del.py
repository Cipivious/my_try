class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.f = open("./student.py")

    def __del__(self):
        self.f.close()
        print("删除方法被调用！")


stu = Student("张三", "18")
a = stu
del stu
print("----------------")
