import asyncio
import time


async def do_some_work(x):
    print("等待", x)
    await asyncio.sleep(x)
    return "等待时间为{}".format(x)


if __name__ == "__main__":
    start_time = time.time()
    tasks = [asyncio.ensure_future(do_some_work(i)) for i in range(1, 10)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print("result is ：{}".format(task.result()))
    end_time = time.time()
    print("all time needed is {}".format(end_time - start_time))
