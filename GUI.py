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
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_host, server_port))
server.listen(2)

l1=Label(window, text=time.ctime(time.time()) ,background="blue",foreground="black",relief =SUNKEN,fg="black",bg="gray65")
l1.config(font=("Courier", 10))
l1.pack()

client_data, client_addr = server.accept()
l2 = Label(window, text="Type message  ", relief=RAISED, fg="black", bg="gray65")
l2.place(x=10, y=370)

message=StringVar()
msg_recv = client_data.recv(1024)
l1=Label(window, text=msg_recv ,background="gray67",foreground="black",relief =SUNKEN,fg="black",bg="gray65")
l1.config(font=("Courier", 10))
l1.pack(anchor="nw")

def recive():
    msg_recv = client_data.recv(1024)
    l1 = Label(window, text=msg_recv,background="gray67",foreground="black", relief=SUNKEN, fg="black", bg="gray65")
    l1.config(font=("Courier", 10))
    l1.pack(anchor="nw")
    return

def send_message():
    mtext = message.get()

    l=Label(window, text=mtext, background="DarkSeaGreen1",foreground="black",relief=RAISED, fg="black", bg="gray65")
    l.config(font=("Courier", 10))
    l.pack(anchor="ne")
    client_data.send(mtext)
    return

button = Button(window,text="send",command = send_message)
button.place(x=390, y=395)


entry = Entry(window,width=30,textvariable=message)
entry.place(x=0, y=400)

utton = Button(window,text="new message",command = recive)
utton.place(x=350, y=350)

window.mainloop()