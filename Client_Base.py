import socket

# Creazione del socket con indirizzo di connessione al server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

# Inserimento del messaggio e invio al server
messaggio = input("Inserisci il messaggio: ")
client.send(messaggio.encode())

# Ricezione della risposta del server
risposta = client.recv(1024).decode()
print("Risposta del server: ", risposta)

# Chiusura del client
client.close()