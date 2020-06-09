import time
import threading
def say_hello(thread_name,nb_repeat):
    for x in range(nb_repeat):
        print(thread_name,": hello")
        time.sleep(1)

th1=threading.Thread(target=say_hello,args=("Thread1",30),daemon=True)
th2=threading.Thread(target=say_hello,args=("Thread2",30),daemon=True)
th1.start()
th2.start()


say_hello("main thread",1)
th1.join()
th2.join()