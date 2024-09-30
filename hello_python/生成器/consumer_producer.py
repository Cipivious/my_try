def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("[Consumer] consuming {}".format(n))
        r = "200 OK"


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[Producer] Producing {}".format(n))
        r = c.send(n)
        print("[Producer] received {}".format(r))


c = consumer()
producer(c)
