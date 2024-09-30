import threading


class Kongbaige(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="空白哥")
        self.cond = cond

    def run(self):
        self.cond.acquire()  # 获取锁
        print(f"{self.name}: 一只穿云箭")  # 使用 self.name 替代 getName()
        self.cond.notify()  # 通知另一个线程继续
        self.cond.wait()  # 等待另一个线程的通知
        print(f"{self.name}: 山无棱，天地合")  # 使用 self.name 替代 getName()
        self.cond.notify()  # 通知另一个线程继续
        self.cond.release()  # 确保释放锁
        # try:
        #     print(f"{self.name}: 一只穿云箭")  # 使用 self.name 替代 getName()
        #     self.cond.notify()  # 通知另一个线程继续
        #     self.cond.wait()  # 等待另一个线程的通知
        #     print(f"{self.name}: 山无棱，天地合")  # 使用 self.name 替代 getName()
        #     self.cond.notify()  # 通知另一个线程继续
        # finally:
        #     self.cond.release()  # 确保释放锁


class Ximige(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="西米哥")
        self.cond = cond

    def run(self):
        self.cond.acquire()  # 获取锁
        self.cond.wait()  # 等待第一个线程的通知
        print(f"{self.name}: 千军万马来相见")  # 使用 self.name 替代 getName()
        self.cond.notify()  # 通知第一个线程继续
        self.cond.wait()  # 等待第一个线程的最终通知
        print(f"{self.name}: 乃敢与君绝")  # 使用 self.name 替代
        self.cond.release()  # 确保释放锁
        # try:
        #     self.cond.wait()  # 等待第一个线程的通知
        #     print(f"{self.name}: 千军万马来相见")  # 使用 self.name 替代 getName()
        #     self.cond.notify()  # 通知第一个线程继续
        #     self.cond.wait()  # 等待第一个线程的最终通知
        #     print(f"{self.name}: 乃敢与君绝")  # 使用 self.name 替代 getName()
        # finally:
        #     self.cond.release()  # 确保释放锁


if __name__ == "__main__":
    cond = threading.Condition()
    kongbaige = Kongbaige(cond)
    ximige = Ximige(cond)

    ximige.start()
    kongbaige.start()

    kongbaige.join()
    ximige.join()
