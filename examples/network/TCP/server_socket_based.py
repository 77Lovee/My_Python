'''
@Author: Javier
@Date: Nov 20th, 2019

'''
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()    # get servert ip (local)
port = 12345
server.bind((host, port))             # bind the port
server.listen(5)

while True:
    con, addr = server.accept()
    print("connected by: ", addr)
    con.send(b"Thanks for connect me!")
    con.close()


