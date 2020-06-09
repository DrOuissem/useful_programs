import tkinter

window = tkinter.Tk()
window.geometry("300x300+100+100")
listbox = tkinter.Listbox(window)
listbox.pack()
listbox.insert(tkinter.END,"Orange")
listbox.insert(tkinter.END,"Red")
listbox.insert(tkinter.END,"Yellow")
listbox.insert(tkinter.END,"Blue")
listbox.insert(tkinter.END,"Green")
def on_select(event):
    l = event.widget
    index=l.curselection()[0]
    value=l.get(index)
    print(value)

listbox.bind("<<ListboxSelect>>",on_select)

window.mainloop()