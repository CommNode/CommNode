import Get_IP_Address
import socket

'''
1. Creazione del socket del client per potersi connettere
   al server e comunicare con gli altri client.
'''
ip_address = Get_IP_Address.get_local_ip()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, 5000))


'''
2. Ricevo il messaggio di benvenuto dal server
   quando stabilisco la connessione e lo mando
   a video.
'''
risposta_benvenuto = client.recv(1024).decode()
istruzioni_disconnessione = client.recv(1024).decode()
print(risposta_benvenuto)
print(istruzioni_disconnessione)


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
            è pari a 0, altrimenti se il messaggio è exit,
            disconnetto il client dal server
            '''
            if len(messaggio) == 0:
                raise Exception

            if messaggio == "exit":
                break
        except Exception as e:
            print(f"Errore durante l'invio del messaggio!")
finally:
    client.close()