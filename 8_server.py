#8) Write a program to create client and server side sockets and use them to send a string in lowercase from client to the server, the server then converts the string to uppercase and return back to client.

#Server Side

import socket

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen()

print("Server is listening on", server_ip, "port", server_port)

while True:
    client_socket, client_address = server_socket.accept()

    print("Client connected from", client_address)

    lowercase_string = client_socket.recv(1024).decode()

    uppercase_string = lowercase_string.upper()

    client_socket.sendall(uppercase_string.encode())

    client_socket.close()

# Client Side 

import socket

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

lowercase_string = str(input("Enter a String :- "))
lowercase_string = lowercase_string.lower()
client_socket.sendall(lowercase_string.encode())

uppercase_string = client_socket.recv(1024).decode()

print("Uppercase String from Server:", uppercase_string)

client_socket.close()
