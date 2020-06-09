from tkinter import *
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("example.db")
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Students(FN TEXT, LN TEXT, AGE INTEGER,
Email TEXT, Login TEXT, PW TEXT, PRIMARY KEY(Login))
''')
conn.commit()
def login_function():
    login_screen=Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen,text="Please enter your username and password").pack()
    Label(login_screen,text="Username * ").pack()
    login = StringVar()
    user_name_entry=Entry(login_screen,textvariable=login)
    user_name_entry.pack()
    Label(login_screen,text="Password *").pack()
    password=StringVar()
    password_entry=Entry(login_screen,textvariable=password,show='*')
    password_entry.pack()
    def submit_login():
        request=''' SELECT * FROM Students WHERE Login='{}' AND PW='{}'
        '''.format(login.get(),password.get())
        try:
            c.execute(request)
            results=c.fetchall()
            if len(results)==0:
                messagebox.showinfo(title="login",message="incorrect login or password")
            else:
                messagebox.showinfo(title="login", message="Welcome {} {}".format(results[0][0],results[0][1]))
                login_screen.destroy()
        except:
            messagebox.showinfo(title="login", message="Error, please try again")
    Button(login_screen,text="Login",width=10,command=submit_login).pack(pady=50)


def register_function():
    register_screen=Toplevel(main_screen)
    register_screen.title("Register")
    label_text=["First Name","Last Name","Age","Email-Address","Login","Password"]
    list_stringvar=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    list_entry=[]
    list_label=[]
    for x in range(6):
        l=Label(register_screen,text=label_text[x])
        l.grid(row=x,column=0,pady=2,padx=2,sticky=W)
        list_label.append(l)
        e=Entry(register_screen,textvariable=list_stringvar[x])
        e.grid(row=x,column=1,pady=2,padx=2,sticky=E)
    def submit_register():
         request='''INSERT INTO Students ('FN','LN','AGE','Email','Login','PW')
         VALUES('{}','{}',{},'{}','{}','{}')
         '''.format(list_stringvar[0].get(),list_stringvar[1].get(),list_stringvar[2].get(),
                    list_stringvar[3].get(), list_stringvar[4].get(), list_stringvar[5].get() )
         try:
            c.execute(request)
            conn.commit()
            messagebox.showinfo(title="Register",message="Registered Successfully")
            register_screen.destroy()
         except:
             messagebox.showinfo(title="Register", message="Error, Please Try again")
    def reset_function():
        for x in range(6):
            list_stringvar[x].set("")
    submit_button=Button(register_screen,text="Submit",command=submit_register)
    reset_button=Button(register_screen,text="Reset",command=reset_function)
    submit_button.grid(row=6,column=0,pady=20,padx=10,sticky=W)
    reset_button.grid(row=6, column=1, pady=20, padx=10, sticky=E)

main_screen=Tk()
main_screen.title("main screen")
main_screen.geometry("300x250")

login_button=Button(main_screen,text="Login",width=20,command=login_function)
register_button=Button(main_screen,text="Register",width=20,command=register_function)
login_button.grid(row=0,column=0,padx=40,pady=40)
register_button.grid(row=1,column=0,padx=40,pady=40)
main_screen.mainloop()