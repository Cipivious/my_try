import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))

# 使用事件来控制线程间的同步
exit_event = threading.Event()


def input_content():
    try:
        while not exit_event.is_set():
            message = input()
            if message:
                client.send(message.encode())
    except Exception as e:
        print(f"客户端出错: {e}")
    finally:
        exit_event.set()  # 通知其他线程退出
        client.close()


def receive_content():
    try:
        while not exit_event.is_set():
            data = client.recv(8192).decode()
            if data == "886":
                print("连接结束")
                break
            print(f"{data}")
    except Exception as e:
        print(f"客户端出错: {e}")
    finally:
        exit_event.set()  # 通知其他线程退出
        client.close()


input_thread = threading.Thread(target=input_content, args=())
receive_thread = threading.Thread(target=receive_content, args=())

input_thread.start()
receive_thread.start()

input_thread.join()
receive_thread.join()
