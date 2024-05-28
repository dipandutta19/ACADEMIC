#4) Write a server program in python to create server side socket and use it to receive a client side request, process it to generate response in form of current date and time where server program should be running and sent response back to the client

#Server Side

import socket
import datetime

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen()

print("Server is listening on", server_ip, "port", server_port)

while True:
    client_socket, client_address = server_socket.accept()

    print("Client connected from", client_address)
    request = client_socket.recv(1024).decode()

    if request == "GET /date-time":
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = current_datetime.encode()
        client_socket.sendall(response)

    client_socket.close()


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
