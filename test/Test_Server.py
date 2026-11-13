import sys
import os

# Aggiunge la cartella CommNode ai percorsi di ricerca di Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Server.Server import Server

def test_server():
    my_server = Server()

    # Inizializzo il server
    my_server.inizializza_server()

    # Accetto le connessioni client
    my_server.connessione_client()

if __name__ == "__main__":
    test_server()
