import threading
import time

class MyThread (threading.Thread):
    def __init__(self,name_thread,nb_repeat):
        threading.Thread.__init__(self)
        self.name_thread=name_thread
        self.nb_repeat=nb_repeat

    def run(self):
        for x in range(self.nb_repeat):
            print(self.name_thread, ":hello")
            time.sleep(1)

th1= MyThread("thread1",5)
th2= MyThread("thread2",5)
th1.start()
th2.start()