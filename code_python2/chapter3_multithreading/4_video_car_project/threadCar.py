import threading
import time
from tkinter import*
_lock=threading.Lock()
class Car:
    def __init__(self):
        self.speed=0

    def accelerate(self):
        with _lock:
            self.speed+=1
            if self.speed>300:
                self.speed=300
    def decelerate(self):
        with _lock:
            self.speed-=1
            if self.speed<0:
                self.speed=0

class AccelerateThread(threading.Thread):
    def __init__(self,car):
        threading.Thread.__init__(self,daemon=True)
        self.car=car
        self.start()
    def run(self):
        for x in range(100):
            self.car.accelerate()
            time.sleep(0.1)

class DecelerateThread(threading.Thread):
    def __init__(self,car):
        threading.Thread.__init__(self,daemon=True)
        self.car=car
        self.start()
    def run(self):
        for x in range(100):
            self.car.decelerate()
            time.sleep(0.1)

c=Car()

def accelerate_function():
    AccelerateThread(c)

def decelerate_function():
    DecelerateThread(c)

window=Tk()
window.geometry("300x200")
label=Label(window,text="speed:"+str(c.speed))
b1=Button(window,text="accelerate",command=accelerate_function,pady=20)
b2=Button(window,text="decelerate",command=decelerate_function,pady=20)
label.pack()
b1.pack()
b2.pack()
stop_loop=False
def loop():
    while not stop_loop:
        label.configure(text="speed:"+str(c.speed))
        window.update()
        time.sleep(0.1)
window.after(1000,loop)

def on_closing():
    global stop_loop
    stop_loop=True
    window.destroy()
window.protocol("WM_DELETE_WINDOW",on_closing)
window.mainloop()