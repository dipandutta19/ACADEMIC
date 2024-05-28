#1) WAP in Python to find out the ip address of a local machine or any other machine

import socket

def get_local_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        return "Error: {}".format(e)

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        return "Error: {}".format(e)

local_ip = get_local_ip()
print("Local IP Address:", local_ip)

domain = input("Enter the domain name (e.g., www.google.com): ")

domain_ip = get_ip_address(domain)
print("IP Address of", domain + ":", domain_ip)
