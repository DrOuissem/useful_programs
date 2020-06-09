class Shark:
    animal_type = "fish"
    
    def __init__(self,age):
        self.age=age
    def print_info(self):
        print("animal_type:",Shark.animal_type)
        print("age: ",self.age)

Shark.animal_type="bigfish"
shark1 = Shark(2)
shark2 = Shark(3)
shark1.print_info()
shark2.print_info()