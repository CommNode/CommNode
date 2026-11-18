import socket
import threading
from .Get_IP_Address import get_local_ip

"""
Main class for client management
"""
class Client:
    # Initializing the Client class
    def __init__(self):
        self.port = None
        self.ip_address = None
        self.client = None
        self.connected = False

    # Function to create the client and connect it to the server
    def initialize_client(self):
        self.port = 5000
        self.ip_address = get_local_ip()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip_address, self.port))
        self.connected = True

    """
    2. Function that starts receiving the
       messages from the server (welcome, instruction, messages
       from other clients).
       
       Return immediately, so you can continue with send_messages().
    """
    def reception_message(self):
        thread = threading.Thread(target=self._listen_server, daemon=True)
        thread.start()

    """
    Function executed by the receiving thread:
        Accumulate data into a buffer and print a message
        for each line(delimiter \\n)
    """
    def _listen_server(self):
        buffer = ""

        try:
            while self.connected:
                data = self.client.recv(1024)

                # empty recv: server closed connection
                if not data:
                    break

                buffer += data.decode(errors='replace')

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    # print with flush=True to make sure the message
                    # appear immediately and with a clean line before the next prompt
                    print(line, flush=True)
        except OSError:
            pass  # Socket closed locally or connection lost
        finally:
            if self.connected:
                print("\nConnection closed by server! Press Enter to exit.")
            self.connected = False

    """
    3. Function for reading user message
       to be sent to the server, with control to verify
       the desire to disconnect from the server
    """
    def send_message(self):
        try:
            while self.connected:
                message_to_send = input()

                # If the server dropped while writing, you exit
                if not self.connected:
                    break

                if len(message_to_send.strip()) == 0:
                    print("Error: Message cannot be empty!")
                    continue

                try:
                    self.client.send(message_to_send.encode())
                except OSError:
                    print("Error sending message!")
                    break

                if message_to_send.strip().lower() == "exit":
                    break
        finally:
            self.connected = False

            try:
                self.client.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass

            self.client.close()