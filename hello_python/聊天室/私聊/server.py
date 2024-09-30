import socket
import threading
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
print("服务器已经启动：欢迎来聊")
client_list = []
client_list_lock = threading.Lock()  # 锁用于保护 client_list
addr_list = {}


def match_string(input_string):
    pattern = r"(@\S+)\s?(.*)"
    match = re.match(pattern, input_string)
    if match:
        return match.groups()  # 返回匹配到的内容
    else:
        return ("", "")  # 如果没有匹配到，返回空元组


def handle_server(sock, addr):
    try:
        while True:
            print(str(addr[1]) + "发送话语")
            data = sock.recv(1024).decode()
            result = match_string(data)
            print(result)
            if result[0]:
                for addr_list_element, a_sock in addr_list.items():
                    if "@" + str(addr_list_element) == result[0]:
                        a_sock.send((str(addr[1]) + ":" + result[1]).encode())
                        break
                continue
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
                                client.send((str(addr[1]) + ":" + data).encode())
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
        print(sock)
        print(addr)
        with client_list_lock:
            client_list.append(sock)
            addr_list[addr[1]] = sock

        thread = threading.Thread(target=handle_server, args=(sock, addr))
        thread.start()
except KeyboardInterrupt:
    print("服务器正在关闭...")
finally:
    with client_list_lock:
        for client in client_list:
            client.close()
    server.close()
