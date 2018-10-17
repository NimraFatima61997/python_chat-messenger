# TCP socket(client)
import socket
import time

server_host = "127.0.0.1"
server_port = 50561

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name=raw_input("NAME : ")
connected = "false"
while connected != "true":
    try:
       client.connect((server_host,server_port))
       connected = "true"
    except:
        pass

data = ""

while data != "exit":
    data = raw_input("\nTYPE:  ")
    client.send(data)

    if data!="exit":
        server_data=client.recv(1024)
        print "\n", time.ctime(time.time()), "\n<SERVER>  ", server_data