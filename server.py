# USE ON IG1-L...IG5-R

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = ipv4 and SOCK_STREAM = TCP
s.bind(('', 12345))
s.listen(1) # allow for one connection to the socket

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address}")
    clientSocket.send(bytes("Welcome to the server", "utf-8"))