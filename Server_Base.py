import socket

# Creazione del socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000)) # Creazione del socket con l'indirizzo IP locale

# Metto in ascolto il server
server.listen()
print("server in ascolto...")

# Accettazione di una connessione e ricezione del messaggio
connessione, indirizzo = server.accept()
messaggio = connessione.recv(1024).decode()

print(f"Client collegato con l'indirizzo {indirizzo}")
print(f"Messaggio ricevuto: '{messaggio}'")

# Invio ai client di un messaggio di ricezione avvenuto
connessione.send("Messaggio ricevuto!".encode())

# Chiusura del socket e della connessione
connessione.close()
server.close()