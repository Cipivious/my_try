from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

executor = ThreadPoolExecutor(max_workers=3)

num = 1


def get_html(exe_time, i):
    time.sleep(exe_time)
    return i


# for i in range(10):
#     exe_time = random.random()
#     return_num = executor.submit(get_html, exe_time, i)
#     print("线程{}加载完成".format(return_num.result()))

all_tasks = [executor.submit(get_html, random.random(), i) for i in range(10)]

for item in as_completed(all_tasks):
    print("线程{}加载完成".format(item.result()))
