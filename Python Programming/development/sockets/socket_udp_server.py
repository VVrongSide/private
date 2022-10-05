"""
Simple setup of a server with a UDP socket which waits for incomming
data and prints it.

"""

# Libraries to import
import socket

# Variables
PORT = 9001                                 # An arbitrary integer from 1 to 65535.
BUFFER = 1024                               # Buffer size (power of 2).
HOSTNAME = socket.gethostname()             # Gets machine hostname.
SERVER_IP = socket.gethostbyname(HOSTNAME)  # Retrieves machine IP address.
ADDR = (SERVER_IP, PORT)                    # Tuple with server IP and port.

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Intance of a UDP socket obejct.
server.bind(ADDR)                           # Assign port and IP to socket object.

data, addr = server.recvfrom(BUFFER)        # BLOCKING function. Receive data from the socket.
                                                # data = a bytes object representing the data received.
                                                # addr = tuple with client (IP, port).

print(data)                                 # Prints the byte object 'data'.     
