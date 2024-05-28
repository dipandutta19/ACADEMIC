# Client Side 

import socket

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

message = "Hello, Echo Server!"
client_socket.sendall(message.encode())

response = client_socket.recv(1024).decode()

print("Server Response:", response)

client_socket.close()