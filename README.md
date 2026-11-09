# CommNode

Python client-server socket utility with threaded concurrency for real-time network communication.

## Key Features

- Threaded architecture for concurrent client connections
- Broadcast messaging capabilities
- Automatic IP detection
- Cross-platform compatibility
- Modular design for extensibility

## Project Structure

```
CommNode/
├── Client/                 # Package Python per il Client
│   ├── __init__.py         # File di inizializzazione package (vuoto)
│   ├── Client.py           # Contiene la classe che gestisce il Client
│   └── Get_IP_Address.py   # Contiene il codice per ottenere l'indirizzo IP del PC indipendentemente dall'OS
├── Server/                 # Package Python per il Server
│   ├── __init__.py         # File di inizializzazione package (vuoto)
│   └── Server.py           # Contiene la classe che gestisce il Server
├── test/                   # Contiene i test per la verifica delle funzionalità Client-Server
├── .gitignore
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## 🛠️ Technical Specifications

- **Protocol**: TCP/IP sockets
- **Language**: Python 3.x
- **Architecture**: Threaded client-server model
- **Encoding**: UTF-8 with error handling
- **Port**: configurable (default: 5000)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/CommNode.git

# Navigate to project directory
cd CommNode

# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start the server
python Server/Server.py

# Start a client
python Client/Client.py
```

## 💡 Usage

```bash
# Server
python Server/Server.py

# Client
python Client/Client.py
```

Clients can connect and exchange messages. Use `exit` to disconnect voluntarily.

## 👥 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## 📜 License

See [LICENSE](LICENSE) for license rights and limitations.

## 🛡️ Security

See [SECURITY.md](SECURITY.md) for the security policy and reporting procedures.