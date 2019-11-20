
'''
@Author: Javer
@Date: Nov 20th, 2019
'''

import  socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()              # host ip, where the data it should send to , but here host ip and clinet ip are same
port = 12345
while True:
    data = input(">>").strip()
    client.sendto(data.encode(), (host, port))
    print(client.recv(1024).decode())
