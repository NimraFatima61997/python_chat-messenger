from Tkinter import*
import socket
import time
window = Tk()
window.title("CLIENT SIDE")
window.geometry('450x450+700+200')
window.configure(background="black")

server_host = "127.0.0.1"
server_port = 50561
message = StringVar()

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_host, server_port))
print "connected"
l2 = Label(window, text="Type Name  ", relief=RAISED, fg="black", bg="gray65")
l2.place(x=10, y=370)

l1=Label(window, text=time.ctime(time.time()) ,background="blue",foreground="black",relief =SUNKEN,fg="black",bg="gray65")
l1.config(font=("Courier", 10))
l1.pack()

def send_message():
    mtext = message.get()
    l2 = Label(window, text="Type message  ", relief=RAISED, fg="black", bg="gray65")
    l2.place(x=10, y=370)
    l3 = Label(window, text=mtext,background="DarkSeaGreen1",foreground="black",relief=RAISED, fg="black", bg="gray65")
    l3.config(font=("Courier", 10))
    l3.pack(anchor="ne")
    client.send(mtext)
    return


def recive():
    server_data = client.recv(1024)
    l = Label(window, text=server_data,background="gray67",foreground="black", relief=SUNKEN, fg="black", bg="gray65")
    l.config(font=("Courier",10))
    l.pack(anchor="nw")

button = Button(window,text="send",command=send_message)
button.place(x=390,y=395)

entry = Entry(window,width=30,textvariable=message)
entry.place(x=0,y=400)

utton = Button(window,text="new message",command=recive)
utton.place(x=350,y=350)

window.mainloop()