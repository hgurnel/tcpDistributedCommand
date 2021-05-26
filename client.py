import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 12345
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "--no-launcher"
ENCODING_METHOD = "utf-8"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.connect((TCP_IP, TCP_PORT))

clientSocket.send(bytes(MESSAGE_TO_SERVER, ENCODING_METHOD))

serverMessage = (clientSocket.recv(BUFFER_SIZE)).decode(ENCODING_METHOD)
print("Message from server: " + serverMessage)