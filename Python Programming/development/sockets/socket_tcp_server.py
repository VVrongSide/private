"""
Simple setup of a server with a TCP socket which waits for incomming connections
and relays back to the client.

"""

# Libraries to import
import socket

# Variables
PORT = 9001                                 # An arbitrary integer from 1 to 65535.
BUFFER = 1024                               # Buffer size (power of 2).
HOSTNAME = socket.gethostname()             # Gets machine hostname.
SERVER_IP = socket.gethostbyname(HOSTNAME)  # Retrieves machine IP address.
ADDR = (SERVER_IP, PORT)                    # Tuple with server IP and port.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Intance of a socket obejct.
server.bind(ADDR)                           # Assign port and IP to socket object.
server.listen()                             # Enable the server to accept connections - OPTIONAL: specify backlog.

conn, addr = server.accept()                # BLOCKING execution while waiting for incomming connections.       
                                                # conn = new socket object to client.
                                                # addr = tuple with client (IP, port).

with conn:                                  # Automatically close the socket at the end of this block.
    while True:
        data = conn.recv(BUFFER)            # Receive byte object from socket object. BUFFER specifiy max received data at once.
        print(data)                         # Prints the byte object 'data'.
        conn.send(b"Hello you!")            # Send a byte object of a string to the client.
        break                               # Exist the while loop and terminate socket connection.

