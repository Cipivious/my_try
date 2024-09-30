from typing import Any


class Student:
    __isinstance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(self)

    def run(self, method):
        if hasattr(self, method):
            try:
                getattr(self, method)()
            except:
                print(getattr(self, method))
        else:
            print("Student 没有这个属性或者方法！")

    # def __repr__(self):
    #     return "class:\t Student\nname:\t {}\nage:\t {}\n".format(self.name, self.age)
    def __repr__(self):
        # self.__getattribute__("age")
        return type(self).__name__ + "[" + str(self.__dict__)[1:-1] + "]"

    def __getattribute__(self, item):
        if item == "age":
            print("又过了一年，{}长大了一岁".format(super().__getattribute__("name")))
            new_age = str(int(super().__getattribute__(item)) + 1)
            super().__setattr__(item, new_age)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("访问未定义的属性")
        return "default"

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "name":
            print("姓名为{}的对象被创建".format(value))
        self.__dict__[name] = value


stu = Student("张三", "18")
print(stu)
print("")
new_stu = Student("李四", "38")
print(stu)

if sorted(stu.__dir__()) == sorted(dir(stu)):
    print("sorted(stu.__dir__()) = sorted(dir(stu))\n")
else:
    print("sorted(stu.__dir__()) ！= sorted(dir(stu))\n")

new_stu.__dict__["gender"] = "男"
print(stu)
print(stu.age)
print(stu)
print(stu.xxx)
print("-----------------------------")
stu.run("say_hello")
stu.run("name")
print("-----------------------------")


def create_baoshu():
    num = None

    def baoshu():
        nonlocal num
        if not num:
            num = 1
        print(num)
        num += 1

    return baoshu


baoshu = create_baoshu()
setattr(stu, "baoshu", baoshu)
for i in range(5):
    stu.baoshu()

delattr(stu, "baoshu")
try:
    stu.baoshu()
except:
    print("stu没有{}这个方法".format('"baoshu"'))
