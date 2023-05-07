import socket

SRV_ADDR = input("Inserire IP server: ")
SRV_PORT = int(input("Inserire porta server: "))

def print_menu():
    print("""\n\n0) Chiudere connessione
1) Informazioni sistema
2) Contenuti directory""")

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))

print("Connessione stabilita")
print_menu()

while 1:
  message = input("\n-Scegli una opzione: ")

  if(message == "0"):
      my_sock.sendall(message.encode())
      my_sock.close()
      break

  elif(message == "1"):
      my_sock.sendall(message.encode())
      data = my_sock.recv(1024)
      if not data: break
      print(data.decode("UTF-8"))

  elif(message == "2"):
      path = input("Inserire il percorso: ")
      my_sock.sendall(message.encode())
      my_sock.sendall(path.encode())
      data = my_sock.recv(1024)
      data = data.encode("UTF-8").split(",")
      print("*"*40)
      for x in data:
          print(x)
      print("*"*40)