import threading
import time
import random


class HtmlProcessor(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(random.random())
        print("URL {} 加载完成".format(self.url))
        self.sem.release()
        return self.url


class UrlProducer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.sem = threading.Semaphore(5)

    def run(self):
        for i in range(20):
            self.sem.acquire()
            htmlprocessor = HtmlProcessor(i, self.sem)
            htmlprocessor.start()


if __name__ == "__main__":
    urlproducer = UrlProducer()
    urlproducer.start()
