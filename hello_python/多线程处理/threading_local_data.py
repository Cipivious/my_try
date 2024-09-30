import threading

local_data = threading.local()

local_data.name = "local_data"


class Mythread(threading.Thread):
    def run(self):
        print("赋值前，子进程", threading.current_thread(), local_data.__dict__)
        local_data.name = self.name
        print("赋值后，子进程", threading.current_thread(), local_data.__dict__)


if __name__ == "__main__":
    print("开始前，主进程", local_data.__dict__)

    t1 = Mythread()
    t1.start()
    t1.join()

    t1 = Mythread()
    t1.start()
    t1.join()

    print("开始后，主进程", local_data.__dict__)
