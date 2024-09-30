import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()

sock, addr = server.accept()
data = sock.recv(1024)

print(data.decode())
sock.send("hello, {}".format(data.decode()).encode())
server.close()
sock.close()
