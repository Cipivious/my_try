list = ["1", 1]

for item in list:
    try:
        print(item + 1)
    except TypeError as e:
        print(e)
    else:
        print("程序运行正常")
    finally:
        print("程序在终止的时候运行")