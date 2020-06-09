from tkinter import *

window=Tk()
w=800
h=500
x=200
y=0
window.geometry("{}x{}+{}+{}".format(w,h,x,y))

menubar = Menu(window)
filemenu = Menu(menubar)
editmenu = Menu(menubar)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)

filemenu.add_command(label="New",command=lambda : print("New"))
filemenu.add_command(label="Open",command=lambda : print("Open"))
filemenu.add_command(label="Save",command=lambda : print("Save"))
filemenu.add_command(label="Save as",command=lambda : print("Save as"))
filemenu.add_separator()
filemenu.add_command(label="Exit",command=lambda : window.quit())

editmenu.add_command(label="Copy",command=lambda : print("Copy"))
editmenu.add_command(label="Paste",command=lambda : print("Paste"))

window.config(menu=menubar)

window.mainloop()
