import socket

'''
1. Creazione del socket del server per accettare 
   successivamente ogni tipo di connessione sulla
   stessa rete.
'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))


'''
2. Metto in ascolto il server per poter far
   connettere i client connessi sulla stessa
   rete del medesimo server.
'''
server.listen()
print("server in ascolto...")


'''
3. Permetto al server di poter far connettere
   N client per poter messaggiare.
'''
try:
    while True:
        # Accetto una connessione client
        connessione, indirizzo = server.accept()

        try:
            print(f"Client collegato con l'indirizzo {indirizzo}")

            """
            1. Invio al client che si connette il messaggio di benvenuto,
               successivamente mando le istruzioni su come disconnettersi
            """
            connessione.send("Benvenuto su CommNode!".encode())
            connessione.send("Scrivere exit per disconnettersi dal server!".encode())

            """
            2. Ricevo un messaggio dal client, se il messaggio è
               "exit" dico che quel client si è disconnesso.
            """
            messaggio = connessione.recv(1024).decode()
            if messaggio.lower() == "exit":
                print(f"Il client con IP {indirizzo} si è disconnesso!")
        except Exception as e:
            print(f"Errore con il client {indirizzo}: {e}")
        finally:
            connessione.close() # Chiusura del socket e della connessione
except KeyboardInterrupt:
    print("\nServer interrotto dall'utente!")
finally:
    server.close()