#5) Given an IP Address and the required subnet. WAP to Find out the subnet mask and subnetwork address of each subnet
import ipaddress
def ipv4_subnet(ip_address, subnet):
    try:
        network = ipaddress.ip_interface(f"{ip_address}/{subnet}")
    except (ValueError,ipaddress.AddressValueError) as e:
        raise ValueError(f"Invalid Ip address or subnet: {e}")
    subnet_mask = str(network.netmask)
    subnetwork_address = str(network.network)
    return subnet_mask,subnetwork_address
ip_address = str(input("Enter the IPv4 address :- "))#(e.g., 192.168.1.0)
subnet = int(input("Enter the required subnet :- "))#(e.g., 24)
try:
    subnet_mask, subnetwork_address = ipv4_subnet(ip_address, subnet)
    print(f"Subnet Mask : {subnet_mask}")
    print(f"Subnetwork Address : {subnetwork_address}")
except ValueError as e:
    print(f"Error : {e}")