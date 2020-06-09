from tkinter import *
import sqlite3
conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Books (TITLE TEXT, AUTHOR TEXT, RELEASE INTEGER, PRICE INTEGER)")
conn.commit()

main_screen=Tk()
main_screen.title("search a book")
buttons=[]
label_text=["Title","Author","Release","Price"]
list_stringvar=[StringVar(),StringVar(),StringVar()]
list_entry=[]
list_label=[]
def search(nb):
    request="SELECT * FROM Books WHERE "+ label_text[nb]+"='" + list_stringvar[nb].get()+"'"
    try:
        c.execute(request)
    except:
        print("error")
    results = c.fetchall()
    if len(results)==0:
        print("no books in the table")
    for row in results:
        for x in range(4):
            print(label_text[x]," : ",row[x],end="    ")
        print()
    pass
for x in range(3):
    l=Label(main_screen,text=label_text[x])
    l.grid(row=x,column=0,pady=2,padx=2 )
    list_label.append(l)
    b = Button(main_screen, text=label_text[x],command=lambda number=x:search(number))
    e=Entry(main_screen,textvariable=list_stringvar[x])
    e.grid(row=x,column=1,pady=2,padx=2 )
    b.grid(row=x,column=2,pady=2,padx=2 )

main_screen.mainloop()