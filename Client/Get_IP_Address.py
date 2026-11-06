import socket

def get_local_ip() -> str:
    """
    Ottengo l'indirizzo IP connettendomi a un IP esterno
    senza inviare pacchetti, costringendo al OS a interrogare
    la tabella di routing e a rivelare l'indirizzo IP
    dell'interfaccia di rete attualmente in uso
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()

    return local_ip