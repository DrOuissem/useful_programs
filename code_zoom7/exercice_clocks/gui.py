import tkinter
from exercice_clocks import utils
import time
import threading

window=tkinter.Tk()
window2=tkinter.Toplevel(window)
window.geometry("300x100+100+100")
window2.geometry("300x100+600+100")
window.title("This is my first window")
v = tkinter.StringVar()
v.set("12:12:55")
v2 = tkinter.StringVar()
v2.set("12:12:55")
l1=tkinter.Label(window,font=("Courier", 44))
l1.pack()

l2=tkinter.Label(window2,font=("Courier", 44))
l2.pack()


class MyThread2(threading.Thread):
    __slots__ = ['__clock','__v','__label']

    def __init__(self,clock,nb_repeat=100,v=None,label=None):
        threading.Thread.__init__(self)
        self.__clock=clock
        self.__nb_repeat=nb_repeat
        self.__v=v
        self.__label=label

    def run(self):
        for x in range(self.__nb_repeat):
            self.__clock.increment_seconds()
            print(self.__clock)
            self.__label['text']=str(self.__clock)
            #self.__v.set()
            time.sleep(1)

c= utils.Clock()
c2= utils.Clock(color='\033[92m')
th1=MyThread2(c,nb_repeat=10,label=l1)
th2=MyThread2(c2,nb_repeat=20,label=l2)
th1.start()
th2.start()

window.mainloop()