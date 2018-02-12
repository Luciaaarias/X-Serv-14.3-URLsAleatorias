#!/usr/bin/python3

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1237))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTLM page
#  (in a loop)

while True:
    numero = random.randint(0, 100000)
    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')

    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                          "<html><body><h1>Hola." +
                          "<a href=\"http://localhost:1237/" + str(numero) + '">Dame otra.</a></h1></body></html>' +
                          "\r\n", "utf-8"))
    recvSocket.close()