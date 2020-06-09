import tkinter

window1 = tkinter.Tk()
window1.geometry("300x300+100+100")
window1.title("window1")
b1=tkinter.Button(window1,text="button1")
b1.pack()
window2 = tkinter.Toplevel()
window2.geometry("300x300+400+100")
window2.title("window2")
b2=tkinter.Button(window2,text="button2")
window3 = tkinter.Toplevel()
window3.geometry("300x300+700+100")
window3.title("window3")
b3=tkinter.Button(window3,text="button3")
b2.pack()
b3.pack()

def click_button1(event):
    window1.withdraw()
    window2.deiconify()
def click_button2(event):
    window2.withdraw()
    window1.deiconify()
b1.bind('<Button-1>',click_button1)
b2.bind('<Button-1>',click_button2)

def click_button3(event):
    tkinter.Toplevel()
b3.bind("<Button-1>",click_button3)
window1.mainloop()