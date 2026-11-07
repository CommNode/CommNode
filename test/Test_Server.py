from Server.Server import Server

def test_server():
    my_server = Server()

    # Inizializzo il server
    my_server.inizializza_server()

    # Accetto le connessioni client
    my_server.connessione_client()

if __name__ == "__main__":
    test_server()