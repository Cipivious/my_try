import threading
import time


class Mythreading(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        print("线程{}已经初始化完成，随时准备启动...".format(self.name))
        self.event.wait()
        print("线程{}开始执行...\n".format(self.name))


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    [threads.append(Mythreading(event)) for i in range(1, 11)]
    event.clear()
    [t.start() for t in threads]
    time.sleep(2)
    event.set()
    [t.join() for t in threads]
