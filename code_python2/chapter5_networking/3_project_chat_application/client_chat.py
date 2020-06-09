from tkinter import *
from tkinter import messagebox
import threading
import socket
buffer_size=1024
class ThreadRecv(threading.Thread):
    def __init__(self,socket,display_area,listbox):
        threading.Thread.__init__(self)
        self.socket=socket
        self.stop=False
        self.display_area=display_area
        self.listbox=listbox
        self.start()
    def run(self):
        try:
            while self.stop==False:
                message=self.socket.recv(buffer_size).decode()
                l=message.split()
                header = l[0]
                if header == "__updateList__":
                    self.listbox.delete(0,END)
                    for x in range(1,len(l)):
                        self.listbox.insert(END,l[x])
                else:
                    self.display_area.config(state=NORMAL)
                    self.display_area.insert(END,message+"\n")
                    self.display_area.config(state=DISABLED)
        except:
            pass
class GUI:
    def __init__(self):
        self.main_window=Tk()
        self.login_window=Toplevel()
        self.login_window.title("login")
        self.login_window.geometry("300x100")
        Label(self.login_window,text="user name").pack()
        self.user_name_entry=Entry(self.login_window)
        self.user_name_entry.pack()
        Button(self.login_window,text="Start",width=10,command=self.submit_login).pack()
        self.main_window.withdraw()
        #main window
        self.display_area=Text(self.main_window,height=20,width=50)
        label_connected=Label(self.main_window,text="connected users")
        self.listbox=Listbox(self.main_window)
        self.my_msg=StringVar()
        self.entry_field=Entry(self.main_window,textvariable=self.my_msg)
        self.display_area.grid(row=1,column=0,columnspan=2,pady=2)
        label_connected.grid(row=0,column=2)
        self.listbox.grid(row=1,column=2,sticky=N,pady=20)
        self.entry_field.grid(row=2,column=0,columnspan=3,sticky=NSEW,pady=4)

        self.entry_field.bind("<Return>",self.submit_message)
        self.display_area.config(state=DISABLED)
        try:
            self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.connect(("127.0.0.1",1234))
            self.th=ThreadRecv(self.socket,self.display_area,self.listbox)
        except:
            print("There is an error during the connection ")
            exit()
        self.main_window.protocol("WM_DELETE_WINDOW",self.delete_window)
        self.main_window.mainloop()
    def delete_window(self):
        self.socket.send("__stop__".encode())
        self.th.stop=True
        self.socket.close()
        self.main_window.destroy()
    def submit_message(self,event):
        msg = self.my_msg.get()
        self.my_msg.set("")
        self.display_area.config(state=NORMAL)
        self.display_area.insert(END,"me: "+msg+"\n")
        self.display_area.config(state=DISABLED)
        self.socket.send(msg.encode())
    def submit_login(self):
        user_name=self.user_name_entry.get()
        self.main_window.title(user_name)
        self.main_window.deiconify()
        self.login_window.destroy()
        messagebox.showinfo(title="Welcome",message="Welcome {} ".format(user_name))
        self.socket.send(user_name.encode())
GUI()