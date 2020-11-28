import tkinter

window = tkinter.Tk()
window.geometry("300x100+400+100")
window.title("First Example")

l1 = tkinter.Label(window,text="Label1")
e1 = tkinter.Entry(window)
b1 = tkinter.Button(window,text="button1")

l1.pack()
e1.pack()
b1.pack()

def click_button(event):
    window.title(e1.get())
b1.bind('<Button-1>',click_button)

def print_text(event):
    l1.config(text=event.widget.get())
e1.bind("<Return>",print_text)
window.mainloop()
