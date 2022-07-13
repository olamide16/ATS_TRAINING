from socket import socket


def find_my_ip():
    my_name = socket.gethostname()
    my_ip_address = socket.gethostbyname(my_name)
    
    return my_ip_address
print('Your IP address is: ')

print(find_my_ip)

import socket
def find_my_ip():
    my_name = socket.gethostname()
    my_ip_address = socket.gethostbyname(my_name)
    return my_ip_address

print("Your IP address is:")
print(find_my_ip())