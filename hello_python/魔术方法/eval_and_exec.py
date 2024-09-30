x = 20


def func():
    y = 10
    print(eval("x+y"))

    print(eval("x+y", {"x": 3, "y": 4}))

    print(eval("x+y", {"x": 1}, {"y": 5}))


func()

# exec("x=3+4")
# print(x)
# exec("a=[]\na.append(3)")
# print(a)
