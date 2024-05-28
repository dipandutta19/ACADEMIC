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