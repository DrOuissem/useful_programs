import tkinter

window = tkinter.Tk()
window.geometry("800x500+200+0")
canvas = tkinter.Canvas(window)
canvas.config(width=300,height=300,background="grey")
canvas.pack()

rec = canvas.create_rectangle(100,50,200,100,fill="yellow")
ovl = canvas.create_oval(100,50,200,100,fill="blue")

circle = canvas.create_oval(50,50,80,80,fill="blue")
line = canvas.create_line(0,250,300,250,fill="red",width=3)
font = ("Arial",20)
text=canvas.create_text(150,200,text="Hello",font=font)
def paint(event):
    x=event.x
    y=event.y
    x1,y1=x-1,y-1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1,y1,x2,y2,fill="green")
canvas.bind("<B1-Motion>",paint)

def animation():
    coords = canvas.coords(circle)
    items = canvas.find_overlapping(coords[0],coords[1],coords[2],coords[3])
    if (len(items))==1:
        canvas.move(circle,0,1)
        canvas.after(1,animation)

b= tkinter.Button(window,text="animation")
b.pack()
def click_button(event):
    animation()
b.bind("<Button-1>",click_button)

window.mainloop()