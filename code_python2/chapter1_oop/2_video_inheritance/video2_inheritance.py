class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_name(self):
        print("name: ",self.name)
    def print_age(self):
        print("age: ",self.age)
class Student(Person):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        self.id=id
    def print_id(self):
        print("id: ",self.id)
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def print_salary(self):
        print("salary: ",self.salary)


S=Student("Ahmad",20,1234)
T=Teacher("Omer",35,20.000)
S.print_name()
S.print_age()
S.print_id()
T.print_name()
T.print_age()
T.print_salary()


