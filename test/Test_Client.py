import sys
import os
from Client.Client import Client

# Adds CommNode folder to Python search paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_client():
    # Creating the client object
    my_client = Client()

    # Client initialization
    my_client.initialize_client()

    # Receiving initial server messages
    my_client.reception_message()

    # Sending a message to the server
    my_client.send_message()

if __name__ == "__main__":
    test_client()