# udp socket( group client)
import socket
import time

server_host = "127.0.0.1"
server_port = 50566

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name=raw_input("NAME : ")
data = ""

while data != "exit":
    data = raw_input("\nTYPE:  ")
    client.sendto(name + ":" + data, (server_host, server_port ))
    server_data, client_addr = client.recvfrom(1024)
    if data!="exit":

        message = server_data.split(":")
        print "\n", time.ctime(time.time()), "\n ", server_data