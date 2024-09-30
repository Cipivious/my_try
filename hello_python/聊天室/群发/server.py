import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
print("服务器已经启动：欢迎来聊")
client_list = []
client_list_lock = threading.Lock()  # 锁用于保护 client_list


def handle_server(sock, addr):
    try:
        while True:
            data = sock.recv(1024).decode()
            if data == "886":
                sock.send("886".encode())
                with client_list_lock:
                    client_list.remove(sock)
                break  # 结束循环，退出线程
            else:
                with client_list_lock:
                    for client in client_list:
                        if client != sock:
                            try:
                                client.send(data.encode())
                            except Exception as e:
                                print(f"发送到客户端时出错: {e}")
                                client_list.remove(client)
                                client.close()
    except Exception as e:
        print(f"与 {addr} 的连接出错: {e}")
    finally:
        sock.close()
        with client_list_lock:
            if sock in client_list:
                client_list.remove(sock)


try:
    while True:
        sock, addr = server.accept()
        with client_list_lock:
            client_list.append(sock)
        thread = threading.Thread(target=handle_server, args=(sock, addr))
        thread.start()
except KeyboardInterrupt:
    print("服务器正在关闭...")
finally:
    with client_list_lock:
        for client in client_list:
            client.close()
    server.close()
