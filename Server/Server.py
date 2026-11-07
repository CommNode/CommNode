import socket

class Server:
    # Inizializzazione della classe Server
    def __init__(self):
        self.server = None
        self.connessione = None
        self.indirizzo = None

    """
    Funzione per poter creare e mettere in ascolto
    il server creando il socket
    """
    def inizializza_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 5000))
        self.server.listen()
        print("Server in ascolto...")

    """
    Funzione che permette al server di accettare
    N connessioni client per poter messaggiare
    """
    def connessione_client(self):
        try:
            while True:
                # Accetto una connessione client
                self.connessione, self.indirizzo = self.server.accept()

                try:
                    print(f"Client connesso con l'indirizzo {self.indirizzo}")

                    # 1. Invio i messaggi iniziali
                    self.connessione.send("Benvenuto su CommNode!".encode())
                    self.connessione.send("Scrivere exit per disconnettersi dal server!".encode())

                    # 2. Ciclo di ricezione continua dei messaggi dal client
                    while True:
                        messaggio = self.connessione.recv(1024).decode().strip()

                        """
                        Controllo se il client si disconnette bruscamente
                        oppure manda una stringa vuota
                        """
                        if not messaggio:
                            break

                        if messaggio.lower() == "exit":
                            print(f"Il client con IP {self.indirizzo} si è disconnesso!", flush=True)
                            break

                except Exception as e:
                    print(f"Errore con il client {self.indirizzo}: {e}")
                finally:
                    self.connessione.close()
        except KeyboardInterrupt:
            print("\nServer interrotto dall'utente!")
        finally:
            self.server.close()