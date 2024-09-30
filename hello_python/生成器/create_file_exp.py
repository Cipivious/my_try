import asyncio
import time
import os


async def create_file(file_name):
    with open("txt_file/" + file_name + ".txt", "w", encoding="utf-8") as f:
        pass
    return file_name + "创建完成！"


if __name__ == "__main__":
    start_time = time.time()
    os.makedirs("txt_file")
    tasks = [
        asyncio.ensure_future(create_file("text" + str(i))) for i in range(1, 10001)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print("result is ：{}".format(task.result()))
    end_time = time.time()
    print("all time needed is {}".format(end_time - start_time))
