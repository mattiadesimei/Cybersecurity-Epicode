import socket
import platform
import os

SRV_ADDR = "" #Inserire IP
SRV_PORT = 12358

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind ((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s.accept()

while 1:
        try:
                data = connection.recv(1024)
                print (data)
        except:continue
        a= data.decode("UTF-8")
        stringa= a.split(sep="\n")
        #print (stringa)
        if(stringa[0] == "1"):
                tosend = platform.platform() + " " + platform.machine()
                connection.sendall(tosend.encode())
        elif(stringa[0] == "2"):
                data = connection.recv(1024)
                try:
                        filelist = os.listdir(data.decode("UTF-8"))
                        tosend = ""
                        for x in filelist:
                            tosend += "," + x
                except:
                        tosend = "Percorso errato"
                connection.sendall(tosend.encode())
        elif(stringa[0] == "0"):
                connection.close()
                connection, address = s.accept()
        else:
                print ("Errore!")