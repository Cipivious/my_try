import socket
import requests

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
print("服务器已经启动：欢迎来聊")
sock, addr = server.accept()


while True:
    data = sock.recv(1024).decode()
    if data == "886":
        sock.send("886".encode())
        break
    print(f"收到来自 {addr} 的消息: {data}")
    answer = input()
    sock.send(answer.encode())

sock.close()
server.close()
