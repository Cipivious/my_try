import socket
import threading


def handle_server(sock, addr):
    try:
        while True:
            data = sock.recv(1024).decode()
            if data == "886":
                sock.send("886".encode())
                break
            print(f"收到来自 {addr} 的消息: {data}")
            answer = input("输入消息发送至客户端：")
            sock.send(answer.encode())
    except Exception as e:
        print(f"与 {addr} 的连接出错: {e}")
    finally:
        sock.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
print("服务器已经启动：欢迎来聊")

try:
    while True:
        sock, addr = server.accept()
        thread = threading.Thread(target=handle_server, args=(sock, addr))
        thread.start()
except KeyboardInterrupt:
    print("服务器正在关闭...")
finally:
    server.close()
