import traceback

class MyValueError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    

def set_age(age):
    if age < 0 or age > 120:
        raise MyValueError("你传入的数值的取值不对，应该在0到120岁之间")
    else:
        print("年龄是：", age)
  
try:        
    set_age(-19)
except MyValueError as e:
    print("自定义异常发生：")
    traceback.print_exc()  # 打印完整的堆栈跟踪信息
