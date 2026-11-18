import sys
import os
from Server.Server import Server

# Adds CommNode folder to Python search paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_server():
    # Creating the server object
    my_server = Server()

    # Server initialization
    my_server.initialize_server()

    # Accepting client connections
    my_server.client_connection()

if __name__ == "__main__":
    test_server()