import tkinter

window=tkinter.Tk()
window.geometry("300x100+100+100")
window.title("This is my first window")
l1=tkinter.Label(window,text="12:12:55")
l1.pack()

window.mainloop()