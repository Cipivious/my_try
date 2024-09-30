import socket

cities = ["上海市", "北京", "天津", "广州", "深圳"]
for city in cities:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    client.send(city.encode())

    data = client.recv(8192)
    print(f"{data.decode()}")
    client.close()
