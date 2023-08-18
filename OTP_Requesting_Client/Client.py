import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12346))

data = client_socket.recv(1024).decode('ascii')

print(data)


