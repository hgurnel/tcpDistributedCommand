import socket
import subprocess

TCP_PORT = 12345
BUFFER_SIZE = 1024
EXECUTABLE = "Z:\\VIRUP\\virup\\VIRUP-0.7-17-gf3cbc46-windows-64bit\\VIRUP.exe"
MESSAGE_TO_CLIENT = "Data received"
ENCODING_METHOD = "utf-8"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', TCP_PORT))
serverSocket.listen(1) # allow for one connection to the server socket

while True:
    conn, address = serverSocket.accept()
    print(f"Connection from client {address}")
    
    arguments = (conn.recv(BUFFER_SIZE)).decode(ENCODING_METHOD)
    print("Message from client: " + arguments)

    conn.send(bytes(MESSAGE_TO_CLIENT, ENCODING_METHOD))

    #command = EXECUTABLE + arguments
    command = EXECUTABLE
    print(f"Command to be executed: {command}")

    subprocess.run([command])

    conn.close()

    break