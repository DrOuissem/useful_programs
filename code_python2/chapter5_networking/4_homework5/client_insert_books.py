from tkinter import *
import socket
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
insert_screen=Tk()
insert_screen.title("Insert new book")
label_text=["Title","Author","Release date","Price"]
list_stringvar=[StringVar(),StringVar(),StringVar(),StringVar()]
list_entry=[]
list_label=[]
for x in range(4):
    l=Label(insert_screen, text=label_text[x])
    l.grid(row=x,column=0,pady=2,padx=2,sticky=W)
    list_label.append(l)
    e=Entry(insert_screen, textvariable=list_stringvar[x])
    e.grid(row=x,column=1,pady=2,padx=2,sticky=E)
def insert_book():
     #send the correct message to the server
     # --- is used as a separator
     request='{}---{}---{}---{}'.format(list_stringvar[0].get(),list_stringvar[1].get(),list_stringvar[2].get(),
                list_stringvar[3].get())
     s.send(request.encode())
     receive = s.recv(buffer_size).decode()
     print(receive)

submit_button=Button(insert_screen, text="Submit", command=insert_book)

submit_button.grid(row=6,column=0,columnspan=2,pady=20,padx=10 )
insert_screen.mainloop()