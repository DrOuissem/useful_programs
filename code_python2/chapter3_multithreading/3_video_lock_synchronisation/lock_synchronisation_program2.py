import threading
import time
_lock = threading.Lock()
class Car:
    def __init__(self):
        self.speed = 0
    def change_speed(self, a):
        with _lock:
            self.speed = self.speed + a
class MyThread(threading.Thread):
    def __init__(self, car, a):
        threading.Thread.__init__(self)
        self.car = car
        self.a = a
        self.start()
    def run(self):
        for x in range(100000):
            self.car.change_speed(self.a)
car = Car()
print("speed before changing:", car.speed)
th1 = MyThread(car, 1)
th2 = MyThread(car, -1)
th1.join()
th2.join()
print("speed after changing:", car.speed)





