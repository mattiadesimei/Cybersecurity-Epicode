#UDP SOCKET

import socket

SRV_ADDR = "192.168.50.101"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SRV_ADDR, SRV_PORT))


print("Server Started! Waiting for connection to port 44444 ... ")

while 1:
        try:
                data, addr = s.recvfrom(1024)
                print(data, "received from: ", addr)
        except socket.error as e:
                error = e
