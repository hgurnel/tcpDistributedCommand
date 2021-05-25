# USE ON IG1-L...IG5-R

import socket
import subprocess

EXECUTABLE = "VIRUP.exe "
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))
s.listen(1) # allow for one connection to the socket

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address}")
    clientSocket.send(bytes("Welcome to the server", "utf-8"))
    
    clientData = s.recv(BUFFER_SIZE)
    print(clientData)
    clientSocket.send(bytes("Data received by server", "utf-8"))
