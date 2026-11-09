import socket
import threading
from .Get_IP_Address import get_local_ip

"""
Classe principale per la gestione del client
"""
class Client:
    def __init__(self):
        self.client = None
        self.connesso = False

    # Funzione per creare il client e connetterlo al server
    def inizializza_client(self):
        port = 5000
        ip_address = get_local_ip()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip_address, port))
        self.connesso = True

    """
    2. Funzione che avvia in background la ricezione dei
       messaggi dal server (benvenuto, istruzione, messaggi
       dagli altri client).
       
       Ritorna subito, cosi può proseguire con invia_messaggi().
    """
    def ricezione_messaggio(self):
        thread = threading.Thread(target=self._ascolta_server, daemon=True)
        thread.start()

    """
    Funzione eseguita dal thread di ricezione:
        Accumula i dati in un buffer e stampa un messaggio
        per ogni riga(delimitatore \\n)
    """
    def _ascolta_server(self):
        buffer = ""

        try:
            while self.connesso:
                dati = self.client.recv(1024)

                # recv vuoto: il server ha chiuso la connessione
                if not dati:
                    break

                buffer += dati.decode(errors='replace')

                while "\n" in buffer:
                    riga, buffer = buffer.split("\n", 1)
                    # stampo con flush=True per assicurarmi che il messaggio
                    # appaia subito e con un a capo pulito prima del prossimo prompt
                    print(riga, flush=True)
        except OSError:
            pass  # Socket chiuso localmente o connessione persa
        finally:
            if self.connesso:
                print("\nConnessione chiusa dal server! Premi Invio per uscire.")
            self.connesso = False

    """
    3. Funzione per la lettura del messaggio dell'utente
       da inviare al server, con controllo per verificare
       la volontà di disconnessione dal server
    """
    def invia_messaggio(self):
        try:
            while self.connesso:
                messaggio_da_inviare = input()

                # Se il server è caduto mentre si scrive, si esce
                if not self.connesso:
                    break

                if len(messaggio_da_inviare.strip()) == 0:
                    print("Errore: il messaggio non può essere vuoto!")
                    continue

                try:
                    self.client.send(messaggio_da_inviare.encode())
                except OSError:
                    print("Errore durante l'invio del messaggio!")
                    break

                if messaggio_da_inviare.strip().lower() == "exit":
                    break
        finally:
            self.connesso = False

            try:
                self.client.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass

            self.client.close()