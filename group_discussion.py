# udp socket( group server)
import socket
import sys
import time

server_host = "127.0.0.1"
server_port = 50566
group=[]
# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#  if fail to bind socket to host,port then exit the system
try:
    server.bind((server_host, server_port))
except:
    print "failed"
    sys.exit()
print "successfully binned"


while 1:
    client_data, client_addr = server.recvfrom(1024)
    message=client_data.split(":")
    if client_addr not in group:
        group.append(client_addr)
    if message[1] == 'exit':
        print "\n", time.ctime(time.time()), "\n", client_data, "\n", "client disconnected"
    else:
        print "\n", time.ctime(time.time()), "\n",  client_data
        for clients in group:
            if clients !=client_addr:
                server.sendto(client_data, clients)

