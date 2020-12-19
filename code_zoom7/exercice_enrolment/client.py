from tkinter import *
import tkinter.messagebox
import socket
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
enroll_screen=Tk()
enroll_screen.title("Enroll in Python Program")
label_text=["First Name","Last Name","Age","ID"]
list_stringvar=[StringVar(),StringVar(),StringVar(),StringVar()]
list_entry=[]
list_label=[]
for x in range(4):
    l=Label(enroll_screen, text=label_text[x])
    l.grid(row=x,column=0,pady=2,padx=2,sticky=W)
    list_label.append(l)
    e=Entry(enroll_screen, textvariable=list_stringvar[x])
    e.grid(row=x,column=1,pady=2,padx=2,sticky=E)
def is_all_filled():
    for v in list_stringvar:
        if v.get()=='':
            return False
    return True
def enroll_student():

     #send the correct message to the server
     if is_all_filled():
         # --- is used as a separator
         request='{}---{}---{}---{}'.format(list_stringvar[0].get(),list_stringvar[1].get(),list_stringvar[2].get(),
                    list_stringvar[3].get())
         s.send(request.encode())
         receive = s.recv(buffer_size).decode()
         tkinter.messagebox.showinfo(title='received', message=receive)
     else:
         tkinter.messagebox.showinfo(title='error', message='please fill all the blanks')




submit_button=Button(enroll_screen, text="Enroll", command=enroll_student)

submit_button.grid(row=6,column=0,columnspan=2,pady=20,padx=10 )

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        s.send('quit'.encode())
        s.close()
        enroll_screen.destroy()

enroll_screen.protocol("WM_DELETE_WINDOW", on_closing)
enroll_screen.mainloop()