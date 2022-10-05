"""
A client connects to a server through a TCP socket. After connection is established,
a message is sent to the server and then waits for a relay from the server.

"""

# Libraries to import
import socket

# Variables
PORT = 9001                     # An arbitrary integer from 1 to 65535.
BUFFER = 1024                   # Buffer size (power of 2).
SERVER_IP = '127.0.1.1'         # Server IP address.
ADDR = (SERVER_IP, PORT)        # Tuple with server IP and port.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Instance of a socket object.

client.connect(ADDR)            # Connect to a remote socket at ADDR.
client.send(b"Hello Wolrd!")    # Send data to the connected socket.

data = client.recv(BUFFER)      # Waits for a relay from the server.
print(data)                     # Prints the byte object relay from the server.