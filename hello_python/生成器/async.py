import asyncio


async def hello(x):
    await asyncio.sleep(x)
    return x


def callback(task):
    # 获取任务的结果
    result = task.result()
    sum = 10
    print("回调的结果相加等于{}".format(sum + result))


async def main():
    core = hello(2)
    task = asyncio.ensure_future(core)
    task.add_done_callback(callback)
    await task


# 在Python 3.7+中，直接使用 asyncio.run() 来运行主协程
if __name__ == "__main__":
    asyncio.run(main())
