"""
A client sents a message to a server with a UDP socket object.

"""

# Libraries to import
import socket

# Variables
PORT = 9001                     # An arbitrary integer from 1 to 65535.
BUFFER = 1024                   # Buffer size (power of 2).
SERVER_IP = '127.0.1.1'         # Server IP address.
ADDR = (SERVER_IP, PORT)        # Tuple with server IP and port.
MESSAGE = b'Hello World!'       # Message in byte format

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # Instance of a UDP socket object.

client.sendto(MESSAGE,ADDR)     # Sends 'MESSAGE' to the server address 'ADDR' with UDP.
