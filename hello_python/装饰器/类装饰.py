class MyDecorator:
    def __init__(self, func):
        self.func = func  # 保存被装饰的函数

    def __call__(self, *args, **kwargs):
        # 在调用函数之前执行一些操作
        print("Before calling the function")

        result = self.func(*args, **kwargs)  # 调用被装饰的函数

        # 在调用函数之后执行一些操作
        print("After calling the function")

        return result


@MyDecorator
def my_function():
    print("The function is being called.")


my_function()
