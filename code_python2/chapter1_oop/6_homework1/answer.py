#this a porposed correction of homework1. It's not the only possible code.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def print_perimeter(self):
        pass
    @abstractmethod
    def print_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_perimeter(self):
        print("Rectangle perimeter : ",2*(self.a+self.b))

    def print_area(self):
        print("Rectangle area : ", (self.a * self.b))

class Circle(Shape):
    def __init__(self, r):
        self.r=r

    def print_perimeter(self):
        print("Circle perimeter : ", 2 * (self.r * 3.14))

    def print_area(self):
        print("Circle area : ", (self.r * self.r)*3.14)

