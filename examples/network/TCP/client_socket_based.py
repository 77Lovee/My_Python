
'''
@Author: Javer
@Date: Nov 20th, 2019
'''

import  socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                  # clinet ip
port = 12345                                  # must be same to the  port of server
client.connect((host, port))
print(client.recv((1024)))
client.close()