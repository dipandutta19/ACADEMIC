# Client Side 

import socket
import struct

multicast_group = '224.3.29.71'
server_port = 10000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.bind(('', server_port))

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print("\nWaiting to receive message...")
    data, address = client_socket.recvfrom(1024)
    
    print("Received", len(data), "bytes from", address)
    print("Message:", data.decode())