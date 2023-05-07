import socket

#Creazione del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Indirizzo IP e la porta del server
server_address = ('127.0.0.1', 1234)

# Associamo il socket all'indirizzo IP
server_socket.bind(server_address)

# Mettiamo in ascolto il socket sulla porta del server
server_socket.listen()

print(f"In attesa di connessione su {server_address[0]}:{server_address[1]}...")

# Accettiamo la connessione quando un client si connette al server
client_socket, client_address = server_socket.accept()

print(f"Connessione accettata da {client_address[0]}:{client_address[1]}")

# Riceviamo i dati dal client
data = client_socket.recv(1024)

print(f"Dati ricevuti dal client : {data.decode()}")
