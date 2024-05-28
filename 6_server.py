
# 6) Write client-server interaction programs to implement multicasting

#Server Side


import socket
import struct

multicast_group = '224.3.29.71'
server_port = 10000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ttl = struct.pack('b', 1)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

message = "Hello, multicast world!"

try:
    print("Sending message:", message)
    sent = server_socket.sendto(message.encode(), (multicast_group, server_port))
    
finally:
    server_socket.close()
