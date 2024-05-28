#3)Write a server program to implement selective repeat ARQ.

import socket
import threading
import time
import random

WINDOW_SIZE = 4
PACKET_SIZE = 1024
TIMEOUT = 2  
MAX_SEQ = 8

class SelectiveRepeatServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.buffer = [None] * MAX_SEQ
        self.ack_received = [False] * MAX_SEQ
        self.expected_seq = 0

    def simulate_packet_loss(self):
        return random.random() < 0.1

    def receive_packet(self):
        while True:
            try:
                packet, client_addr = self.server_socket.recvfrom(PACKET_SIZE)
                seq_num, data = self.unpack_packet(packet)

                if self.simulate_packet_loss():
                    print(f"Simulated loss of packet {seq_num}")
                    continue

                if seq_num in range(self.expected_seq, self.expected_seq + WINDOW_SIZE):
                    print(f"Received packet {seq_num}")
                    self.buffer[seq_num % MAX_SEQ] = data
                    self.ack_received[seq_num % MAX_SEQ] = True
                    ack_packet = self.pack_packet(seq_num, b'ACK')
                    self.server_socket.sendto(ack_packet, client_addr)

                    while self.ack_received[self.expected_seq % MAX_SEQ]:
                        self.ack_received[self.expected_seq % MAX_SEQ] = False
                        self.expected_seq += 1

            except socket.timeout:
                print("Timeout, waiting for packets...")

    def pack_packet(self, seq_num, data):
        return seq_num.to_bytes(1, 'big') + data

    def unpack_packet(self, packet):
        seq_num = int.from_bytes(packet[0:1], 'big')
        data = packet[1:]
        return seq_num, data

    def start(self):
        print(f"Server started at {self.host}:{self.port}")
        self.server_socket.settimeout(TIMEOUT)
        threading.Thread(target=self.receive_packet).start()

if __name__ == "__main__":
    server = SelectiveRepeatServer()
    server.start()