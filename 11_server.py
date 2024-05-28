#11) Write a program to create client & Server Side Sockets & use them to implement Echo Server

#Server Side

import socket

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen()

print("Echo Server is listening on", server_ip, "port", server_port)

while True:
    client_socket, client_address = server_socket.accept()

    print("Client connected from", client_address)

    message = client_socket.recv(1024).decode()

    client_socket.sendall(message.encode())

    client_socket.close()


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
