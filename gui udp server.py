from Tkinter import*
import socket
import time

window = Tk()
window.title("SERVER SIDE")
window.geometry('450x450+100+200')
window.configure(background="black")

server_host = "127.0.0.1"
server_port = 50561

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((server_host, server_port))


l1=Label(window, text=time.ctime(time.time()) ,background="blue",foreground="black",relief =SUNKEN,fg="black",bg="gray65")
l1.config(font=("Courier", 10))
l1.pack()


group=[]
message=StringVar()
client_data, client_addr = server.recvfrom(1024)
l1=Label(window, text=client_data ,background="gray67",foreground="black",relief =SUNKEN,fg="black",bg="gray65")
l1.config(font=("Courier", 10))
l1.pack(anchor="nw")

def recive():
    client_data, client_addr = server.recvfrom(1024)

    l1 = Label(window, text=client_data,background="gray67",foreground="black", relief=SUNKEN, fg="black", bg="gray65")
    l1.config(font=("Courier", 10))
    l1.pack(anchor="nw")
    return

def send_message():
    mtext = message.get()

    l=Label(window, text=mtext, background="DarkSeaGreen1",foreground="black",relief=RAISED, fg="black", bg="gray65")
    l.config(font=("Courier", 10))
    l.pack(anchor="ne")
    server.sendto(mtext, client_addr)
    return

button = Button(window,text="send",command = send_message)
button.place(x=390, y=395)
entry = Entry(window,width=30,textvariable=message)
entry.place(x=0, y=400)

utton = Button(window,text="new message",command = recive)
utton.place(x=350, y=350)

window.mainloop()