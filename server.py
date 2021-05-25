### IG1-IG5 side
##
##import socket
##
###hostname=socket.gethostname()   
###TCP_IP=socket.gethostbyname(hostname) 
##
##TCP_IP = '192.168.1.61'
##TCP_PORT = 12345
##BUFFER_SIZE = 1024
##COMMAND = "VIRUP.exe"
##
##s = socket.create_server((TCP_IP, TCP_PORT))
##
###s.listen(1)
##
##conn, addr = s.accept()
##
##result = conn.recv(BUFFER_SIZE)
##str(result)
##
##cmd = COMMAND + str(result)
##
###conn.close()


##import socket
##
##
##TCP_IP = '192.168.1.61'
##TCP_PORT = 5005
##BUFFER_SIZE = 1024
##
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind((TCP_IP, TCP_PORT))
##s.listen(1)
##
##conn, addr = s.accept()
##print 'Connection address:', addr
##while 1:
##    data = conn.recv(BUFFER_SIZE)
##    if not data: break
##    print "received data:", data
##    conn.send(data)  # echo
##conn.close()


import time
timeout = time.time() + 5   # 5s from now
test = 0
while True:
    print(test)
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
