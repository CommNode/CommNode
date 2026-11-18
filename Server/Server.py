import socket
import threading

"""
Main class for server management
"""
class Server:
    # Initializing the Server class
    def __init__(self):
        self.server = None
        self.client_connected = {}
        self.lock = threading.Lock()
        self.in_execution = True
        self.ip = "0.0.0.0"
        self.port = 5000

    """
    1. Function to be able to create and listen
       the server by creating the socket
    """
    def initialize_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        self.server.settimeout(1.0)
        print("Server listening...")

    """
    2. Function that accepts N client connections:
           For each new client connection,
           I create a dedicated thread
    """
    def client_connection(self):
        try:
            while self.in_execution:
                try:
                    conn, addr = self.server.accept()
                except socket.timeout:
                    continue

                # I register the client in the shared structure
                with self.lock:
                    self.client_connected[conn] = addr

                thread = threading.Thread(
                    target=self.manage_client,
                    args=(conn, addr),
                    daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\nUser-interrupted server!")
        except Exception as e:
            # Other unexpected exceptions are logged but do not block the shutdown
            print(f"Unexpected error in server: {e}")
        finally:
            self.close_server()

    """
    3. Function executed by a thread for each client:
           Manages messages from that particular
           client connected to the server.
    """
    def manage_client(self, conn, addr):
        try:
            print(f"Client connected with the address {addr}")

            """
            Initial welcome message and instruction
            on how to log out of the server
            """
            conn.sendall(
                "Welcome to CommNode!\n"
                "Write exit to log out of the server!\n".encode()
            )

            while True:
                message = conn.recv(1024).decode().strip()

                # Client disconnected abruptly or empty string
                if not message:
                    break

                # Voluntary client disconnection from the server
                if message.lower() == "exit":
                    print(f"The client with IP {addr} has disconnected from the server!", flush=True)
                    break

                # I forward the message to other clients
                self.broadcast(f"\n{addr[0]}:{addr[1]} > {message}\n", conn)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            print(f"Lost connection with client {addr}")
        except Exception as e:
            print(f"Error with client {addr}: {e}")
        finally:
            # Removing the client from the shared structure
            with self.lock:
                self.client_connected.pop(conn, None)
            conn.close()

    """
    4. Function that sends a message to everyone
       connected clients except the sender
    """
    def broadcast(self, message, sender):
        with self.lock:
            recipients = list(self.client_connected.keys())

        for client in recipients:
            if client is sender:
                continue
            try:
                client.sendall(message.encode())
            except OSError:
                pass  # Client already dropped: will be removed from its thread

    """
    5. Function for orderly server closure
    """
    def close_server(self):
        self.in_execution = False

        with self.lock:
            for client in list(self.client_connected.keys()):
                try:
                    client.close()
                except OSError:
                    pass
            self.client_connected.clear()

        self.server.close()
        print("Closed server.")