import socket
from .Get_IP_Address import get_local_ip

class Client:
    def __init__(self):
        self.client = None

    # Funzione per creare il client e connetterlo al server
    def inizializza_client(self):
        port = 5000
        ip_address = get_local_ip()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip_address, port))

    """
    2. Funzione per ricevere dal server i seguenti messaggi:
        - Messaggio di benvenuto
        - Istruzioni per la disconnessione dal server
    """
    def ricezione_messaggio(self):
        messaggio_benvenuto = self.client.recv(1024).decode()
        istruzioni_disconnessione = self.client.recv(1024).decode()

        print(messaggio_benvenuto)
        print(istruzioni_disconnessione)

    """
    3. Funzione per la lettura del messaggio dell'utente
       da inviare al server, con controllo per verificare
       la volontà di disconnessione dal server
    """
    def invia_messaggio(self):
        try:
            while True:
                try:
                    messaggio_da_inviare = input("Inserisci il messaggio da inviare: ")

                    """
                    Lancio l'eccezione se la lunghezza del messaggio
                    è pari a 0, altrimenti se il messaggio è "exit",
                    disconnetto il client dal server
                    """
                    if len(messaggio_da_inviare) == 0:
                        raise Exception
                    else:
                        # Invio eseguito una sola volta correttamente
                        self.client.send(messaggio_da_inviare.encode())

                    if messaggio_da_inviare == "exit":
                        break
                except Exception as e:
                    print(f"Errore durante l'invio del messaggio!")
        finally:
            self.client.close()