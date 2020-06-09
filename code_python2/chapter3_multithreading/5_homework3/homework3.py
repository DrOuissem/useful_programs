import threading

def is_prime(n):
    if(n<2):
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return n
def sum_prime(a,b):
    res=0
    for i in range(a, b+ 1):
        res+=is_prime(i)
    return res


class MyThread (threading.Thread):
    def __init__(self,a,b):
        threading.Thread.__init__(self)
        self.a=a
        self.b=b
        self.start()

    def run(self):
        self.result=sum_prime(self.a,self.b)

th1= MyThread(1,333333)
th2= MyThread(333334,666666)
th3= MyThread(666667,1000000)
th1.join()
th2.join()
th3.join()
print("value ",th1.result+th3.result+th2.result)
