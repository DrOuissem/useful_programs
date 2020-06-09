class Car:
    def __init__(self,name,color,speed):
        self.name=name
        self.color=color
        self.speed=speed

    def print_info(self):
        print("name:",self.name)
        print("color:",self.color)
        print("speed:",self.speed)
    def increase_speed(self):
        self.speed+=10
        if self.speed>300:
            self.speed=300
    def decrease_speed(self):
        self.speed-=10
        if self.speed<0:
            self.speed=0

car1=Car("Toyota","white",0)
car2=Car("Mercedes","grey",0)
car1.print_info()
car2.increase_speed()
print("-------------")
car2.print_info()
