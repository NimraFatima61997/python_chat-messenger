# TCP socket  (server)
import socket
import sys
import time

server_host = "127.0.0.1"
server_port = 50561

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  if fail to bind socket to host,port then exit the system
try:
    server.bind((server_host, server_port))
except:
    print "failed"
    sys.exit()
print "successfully binned"
server.listen(2)

client_data, client_addr = server.accept()
msg_recv=""
while msg_recv != 'exit':

    msg_recv=client_data.recv(1024)
    if  msg_recv == 'exit':
        print "\n", time.ctime(time.time()), "\n", client_data, "\n", "client disconnected"
    else:
        print "\n", time.ctime(time.time()), "\n",  client_addr,"> :",msg_recv
        data = raw_input("\nTYPE:  ")
        client_data.send(data)

