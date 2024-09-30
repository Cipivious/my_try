import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))

while True:
    message = input()
    client.send(message.encode())
    data = client.recv(8192).decode()
    if data == "886":
        break
    print(f"收到来自服务器的消息: {data}")

client.close()
