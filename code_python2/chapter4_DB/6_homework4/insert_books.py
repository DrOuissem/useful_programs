from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Books (TITLE TEXT, AUTHOR TEXT, RELEASE INTEGER, PRICE INTEGER)")
conn.commit()


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
     request='''INSERT INTO Books ('TITLE','AUTHOR','RELEASE','PRICE')
     VALUES('{}','{}',{},'{}')
     '''.format(list_stringvar[0].get(),list_stringvar[1].get(),list_stringvar[2].get(),
                list_stringvar[3].get())
     try:
         c.execute(request)
         conn.commit()
         messagebox.showinfo(title="Add Book", message="added successfully")
     except:
        messagebox.showinfo(title="Add Book", message="Error, Please Try again")

submit_button=Button(insert_screen, text="Submit", command=insert_book)

submit_button.grid(row=6,column=0,columnspan=2,pady=20,padx=10 )
insert_screen.mainloop()