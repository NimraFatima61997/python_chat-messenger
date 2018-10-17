# udp socket(client)
import socket
import time

server_host = "127.0.0.1"
server_port = 50568

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name=raw_input("NAME : ")
data = ""

while data != "exit":
    data = raw_input("\nTYPE:  ")
    client.sendto(name + ":" + data, (server_host, server_port ))

    if data!="exit":
        server_data, client_addr = client.recvfrom(1024)
        print "\n", time.ctime(time.time()), "\n<SERVER>  ", server_data