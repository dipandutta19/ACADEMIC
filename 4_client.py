# Client Side 

import socket
server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

request = "GET /date-time"
client_socket.sendall(request.encode())

response = client_socket.recv(1024)

print("Current Date and Time:", response.decode())

client_socket.close()