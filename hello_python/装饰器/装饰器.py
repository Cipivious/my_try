import time


def timer(time_type):

    def outer(func):

        def inner(*args, **kwargs):
            start_time = time.time()
            old_result = func(*args, **kwargs)
            end_time = time.time()
            result = end_time - start_time
            if time_type == "m":
                result = result / 60
            elif time_type == "h":
                result = result / 3600
            elif time_type == "s":
                result = result
            else:
                print("time_type is error!")
            print("runnig time is " + str(result))
            return old_result

        return inner

    return outer


@timer(time_type="s")  # add = timer(time_type="s")(add)
def add(a, b, *args):
    time.sleep(1)
    # a = 2
    # b = 8
    sum = a + b
    for arg in args:
        sum += arg

    return sum


print("the sum is = " + str(add(8, 9, 2, 8, 8)))
