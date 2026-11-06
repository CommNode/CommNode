import socket

'''
1. Creazione del socket del client per potersi connettere
   al server e comunicare con gli altri client.
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))


'''
2. Ricevo il messaggio di benvenuto dal server
   quando stabilisco la connessione e lo mando
   a video.
'''
risposta = client.recv(1024).decode()
print(risposta)


'''
3. Inserimento del messaggio da parte dell'utente
   da inviare al server fino a chiusura voluta
   della connessione da parte dell'utente.
'''
try:
    while True:
        try:
            messaggio = input("Inserisci il messaggio: ")
            client.send(messaggio.encode())

            '''
            Lancio l'eccezione se la lunghezza del messaggio
            è pari a 0
            '''
            if len(messaggio) == 0:
                raise Exception
        except Exception as e:
            print(f"Errore durante l'invio del messaggio!")
finally:
    client.close()