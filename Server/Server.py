import socket
import threading

"""
Classe principale per la gestione del server
"""
class Server:
    # Inizializzazione della classe Server
    def __init__(self):
        self.server = None
        self.client_connessi = {}
        self.lock = threading.Lock()
        self.in_esecuzione = True

    """
    1. Funzione per poter creare e mettere in ascolto
       il server creando il socket
    """
    def inizializza_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(("0.0.0.0", 5000))
        self.server.listen()
        self.server.settimeout(1.0)
        print("Server in ascolto...")

    """
    2. Funzione che accetta N connessioni client:
           Per ogni nuova connessione client,
           creo un thread dedicato
    """
    def connessione_client(self):
        try:
            while self.in_esecuzione:
                try:
                    conn, addr = self.server.accept()
                except socket.timeout:
                    continue

                # Registro il client nella struttura condivisa
                with self.lock:
                    self.client_connessi[conn] = addr

                thread = threading.Thread(
                    target=self.gestisci_client,
                    args=(conn, addr),
                    daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\nServer interrotto dall'utente!")
        except Exception:
            # Altre eccezioni impreviste vengono registrate ma non bloccano l'arresto
            print("Errore imprevisto nel server!")
        finally:
            self.chiudi_server()

    """
    3. Funzione eseguita da un thread per ogni client:
           Gestisce i messaggi di quel determinato
           client connesso al server.
    """
    def gestisci_client(self, conn, addr):
        try:
            print(f"Client connesso con l'indirizzo {addr}")

            """
            Messaggio iniziale di benvenuto ed istruzione
            su come disconnettersi dal server
            """
            conn.sendall(
                "Benvenuto su CommNode!\n"
                "Scrivere exit per disconnettersi dal server!\n".encode()
            )

            while True:
                messaggio = conn.recv(1024).decode().strip()

                # Client disconnesso bruscamente o stringa vuota
                if not messaggio:
                    break

                # Disconnessione volontaria del client dal server
                if messaggio.lower() == "exit":
                    print(f"Il clienti con IP {addr} si è disconnesso dal server!", flush=True)
                    break

                # Inoltro il messaggio agli altri client
                self.broadcast(f"\n{addr[0]}:{addr[1]} > {messaggio}\n", conn)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            print(f"Connessione persa con il client {addr}")
        except Exception as e:
            print(f"Errore con il client {addr}: {e}")
        finally:
            # Rimozione del client dalla struttura condivisa
            with self.lock:
                self.client_connessi.pop(conn, None)
            conn.close()

    """
    4. Funzione che invia un messaggio a tutti
       i client connessi tranne al mittente
    """
    def broadcast(self, messaggio, mittente):
        with self.lock:
            destinatari = list(self.client_connessi.keys())

        for client in destinatari:
            if client is mittente:
                continue
            try:
                client.sendall(messaggio.encode())
            except OSError:
                pass  # Client già caduto: verrà rimosso dal suo thread

    """
    5. Funzione per la chiusura ordinata del server
    """
    def chiudi_server(self):
        self.in_esecuzione = False

        with self.lock:
            for client in list(self.client_connessi.keys()):
                try:
                    client.close()
                except OSError:
                    pass
            self.client_connessi.clear()

        self.server.close()
        print("Server chiuso.")