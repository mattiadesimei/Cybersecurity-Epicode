import socket

SRV_ADDR = "" # Inserire IP
SRV_PORT = "" # Inserire Porta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_DGRAM se connesione UDP
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server in linea! Connessione in attesa...")
connection, address = s.accept()
print("Client connesso con l'indirizzo ", address)
while 1:
  data = connection.recv(1024)
  if not data: break
  #connection.sendall(b"Ricezione completata\n")
  print(data.decode("UTF-8"))
connection.close()