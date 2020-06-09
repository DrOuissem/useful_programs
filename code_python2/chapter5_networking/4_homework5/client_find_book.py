from tkinter import *
import socket

buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))

main_screen=Tk()
main_screen.title("search a book")
buttons=[]
label_text=["Title","Author","Release","Price"]
list_stringvar=[StringVar(),StringVar(),StringVar()]
list_entry=[]
list_label=[]
def search(nb):
    if (len(list_stringvar[nb].get()) == 0):
        print("the field is empty")
    else:
        request="{}---{}".format(label_text[nb],list_stringvar[nb].get())
         #send to the server
        s.send(request.encode())
        receive=s.recv(buffer_size).decode()
        #print the result
        print(receive)


for x in range(3):
    l=Label(main_screen,text=label_text[x])
    l.grid(row=x,column=0,pady=2,padx=2 )
    list_label.append(l)
    b = Button(main_screen, text=label_text[x],command=lambda number=x:search(number))
    e=Entry(main_screen,textvariable=list_stringvar[x])
    e.grid(row=x,column=1,pady=2,padx=2 )
    b.grid(row=x,column=2,pady=2,padx=2 )

main_screen.mainloop()