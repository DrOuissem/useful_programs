class Clock:
    __slots__ = ['__hours','__minutes','__seconds','__color']
    def __init__(self,hours=0,minutes=0,seconds=0,color='\033[94m'):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds
        self.__color=color
    def __str__(self):
        return str(self.__hours)+":"+str(self.__minutes)+":"+str(self.__seconds)
    def increment_seconds(self):
        self.__seconds+=1
        if self.__seconds>=60:
            self.__seconds=0
            self.increment_minutes()
    def increment_minutes(self):
        self.__minutes+=1
        if self.__minutes>=60:
            self.__minutes=0
            self.increment_hours()
    def increment_hours(self):
        self.__hours+=1
        if self.__hours>=24:
            self.__hours=0
import threading
import time
lock=threading.Lock()
class MyThread(threading.Thread):
    __slots__ = ['__clock']
    def __init__(self,clock,nb_repeat=100):
        threading.Thread.__init__(self)
        self.__clock=clock
        self.__nb_repeat=nb_repeat
    def run(self):
        for x in range(self.__nb_repeat):
            with lock:
                self.__clock.increment_seconds()
                print(self.__clock)
            time.sleep(1)