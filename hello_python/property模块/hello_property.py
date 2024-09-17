import random

class HelloPython:
    def __init__(self):
        self._price = random.randint(1, 1000)
     
    @property    
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负值")
        self._price = value

# 使用示例
hello_python_instance = HelloPython()

# 获取 price
print(hello_python_instance.price)

# 设置 price
hello_python_instance.price = 500
print(hello_python_instance.price)

# 尝试设置负值，会引发异常
try:
    hello_python_instance.price = -100
except ValueError as e:
    print(e)  # 输出: "价格不能为负值"
