import threading
import time

class MyThread (threading.Thread):

    def __init__(self,name_thread,nb_repeat):
        threading.Thread.__init__(self)
        self.name_thread=name_thread
        self.nb_repeat=nb_repeat
        self.start()
    def run(self):
        for x in range(self.nb_repeat):
            with MyThread._lock:
                print(self.name_thread, ":hello")
            time.sleep(1)

th1= MyThread("thread1",5)
th2= MyThread("thread2",5)