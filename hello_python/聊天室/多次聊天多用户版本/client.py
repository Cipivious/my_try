import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))

try:
    while True:
        message = input()
        client.send(message.encode())
        data = client.recv(8192).decode()
        if data == "886":
            print("连接结束")
            break
        print(f"收到来自服务器的消息: {data}")
except Exception as e:
    print(f"客户端出错: {e}")
finally:
    client.close()
