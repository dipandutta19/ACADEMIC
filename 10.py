#10)Write a program to implement the following. Input an IP address in either dotted decimal or binary format & print the class of the IP Address as well as the corresponding network address.

binary_ip = input("Enter the binary IP address: ")
octets = binary_ip.split(".")
decimal_ip = ""
for octet in octets:
    decimal_ip += str(int(octet, 2)) + "."
print("The decimal IP address is:", decimal_ip)
ip_address=decimal_ip
def ip_info(ip_address):
    octets = ip_address.split('.')
    octets = [int(octet) for octet in octets if octet]
    if octets[0] >= 1 and octets[0] <= 126:
        ip_class = 'A'
        network_id = octets[:1]
    elif octets[0] >= 128 and octets[0] <= 191:
        ip_class = 'B'
        network_id = octets[:2]
    elif octets[0] >= 192 and octets[0] <= 223:
        ip_class = 'C'
        network_id = octets[:3]
    elif octets[0] >= 224 and octets[0] <= 239:
        ip_class = 'D'
        network_id = None
    else:
        ip_class = 'Unknown'
        network_id = None
    return ip_class, network_id
ip_class, network_id = ip_info(ip_address)
print("IPv4 Class:", ip_class)
print("Network ID:", '.'.join(str(octet) for octet in network_id))
