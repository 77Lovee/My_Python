'''
@Author: Javier
@Date Nov 20th, 2019

'''

# UDP: server just send data without connected with client
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.SOCK_DGRAM for UDP
host = socket.gethostname()
port = 12345
server.bind((host, port))

while True:
    data, addr = server.recvfrom(1024)   # addr is the client addr, so the server knows where should data send to
    print(data, addr)
    server.sendto(data.upper(), addr)



