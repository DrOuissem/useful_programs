class Person:
    def __init__(self,name,age,gender,ssn):
        self.name=name
        self.age=age
        self.gender=gender
        self.ssn=ssn

class Student(Person):
    def __init__(self,name,age,gender,ssn,id,gpa):
        super().__init__(name,age,gender,ssn)
        self.id=id
        self.gpa=gpa

def enter_student():
    name=input("Enter student name:")
    age=input("Enter student age:")
    gender=int(input("Enter student gender. Enter 1 if the student is Male, or "
                     "enter 2 if the student is female:"))
    temp="Enter "+name+"'s SSN:"
    ssn=int(input(temp))
    id=int(input("Enter student's ID:"))
    gpa=float(input("Enter student's GPA out of 5:"))
    s=Student(name,age,gender,ssn,id,gpa)
    return s

def print_student(s):
    print("Student name:",s.name)
    print("Age:",s.age)
    if s.gender==1:
        print("Gender: Male")
    else:
        print("Gender: Female")
    print("SSN: ",s.ssn)
    print("Student ID:",s.id)
    print("Student GPA:",s.gpa)


s=enter_student()
print_student(s)