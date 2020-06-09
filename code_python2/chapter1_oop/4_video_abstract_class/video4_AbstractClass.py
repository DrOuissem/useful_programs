from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_name(self):
        print("name: ",self.name)
    def print_age(self):
        print("age: ",self.age)
    @abstractmethod
    def print_info(self):
        pass
class Student(Person):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        self.id=id
    def print_id(self):
        print("id: ",self.id)
    def print_info(self):
        print("Student:\n________")
        Person.print_info(self)
        self.print_id()


class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def print_salary(self):
        print("salary: ",self.salary)
    def print_info(self):
        print("Teacher:\n________")
        Person.print_info(self)
        super().print_info()
        self.print_salary()
#P=Person("Ahmad",20)
S=Student("Ahmad",20,1234)
T=Teacher("Omer",35,20.000)
S.print_info()
T.print_info()


