#7) Given an IP Address, WAP to find out its class network id and host id
def ipv4_info(ip_address):
    octets = ip_address.split('.')
    octets = [int(octet) for octet in octets]
    if octets[0] >= 1 and octets[0] <= 126:
        ip_class = 'A'
        network_id = octets[:1]
        host_id = octets[1:]
    elif octets[0] >= 128 and octets[0] <= 191:
        ip_class = 'B'
        network_id = octets[:2]
        host_id = octets[2:]
    elif octets[0] >= 192 and octets[0] <= 223:
        ip_class = 'C'
        network_id = octets[:3]
        host_id = octets[3:]
    elif octets[0] >= 224 and octets[0] <= 239:
        ip_class = 'D'
        network_id = None
        host_id = None
    else:
        ip_class = 'Unknown'
        network_id = None
        host_id = None

    return ip_class, network_id, host_id
ip_address = str(input("Enter the IPv4 address :- "))#(e.g., 192.168.1.10)
ip_class, network_id, host_id = ipv4_info(ip_address)
print("IPv4 Class:", ip_class)
print("Network ID:", '.'.join(str(octet) for octet in network_id))
print("Host ID:", '.'.join(str(octet) for octet in host_id))