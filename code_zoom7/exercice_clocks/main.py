#Exercice : clock
from exercice_clocks import utils

c= utils.Clock()
c2= utils.Clock(color='\033[92m')
th1= utils.MyThread(c, nb_repeat=10)
th2= utils.MyThread(c2, nb_repeat=20)
th1.start()
th2.start()