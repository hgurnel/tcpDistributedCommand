###!/usr/bin/env python
##
### IG0 side
##
##import socket
##
###hostname=socket.gethostname()   
###TCP_IP=socket.gethostbyname(hostname) 
##
##TCP_IP = '192.168.1.51'
##TCP_PORT = '12345'
##MESSAGE = "--no-launcher"
##
##s = socket.create_connection((TCP_IP, TCP_PORT))
##s.send(bytes(MESSAGE, 'utf8'))



#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.57'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
