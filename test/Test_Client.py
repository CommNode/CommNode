from Client.Client import Client

def test_client():
    my_client = Client()

    # Inizializzo il client
    my_client.inizializza_client()

    # Ricevo i messaggi iniziali del server
    my_client.ricezione_messaggio()

    # Invio un messaggio al server
    my_client.invia_messaggio()

if __name__ == "__main__":
    test_client()