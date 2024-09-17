# 自定义上下文管理器
# import contextlib

# @contextlib.contextmanager
# def test():
#     print("1")
#     yield "xxx"
#     print("2")
    
    
# with test() as test:
#     print("3", test)
import contextlib

@contextlib.contextmanager
def ze():
    try:
        yield
    except ZeroDivisionError as e:
        print(e)

with ze():
    print(1/0)