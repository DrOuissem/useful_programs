


class Person:
    def __init__(self,name,age,gender,ssn):
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__ssn=ssn
    #acessor, getter
    def get_name(self):
        return self.__name
    #mutator (setter)
    def set_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

    def get_ssn(self):
        return self.__ssn
    def set_ssn(self,ssn):
        self.__ssn=ssn


class Student(Person):
    def __init__(self,name,age,gender,ssn,id,gpa):
        super().__init__(name,age,gender,ssn)
        self.__id=id
        self.__gpa=gpa
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self,gpa):
        self.__gpa=gpa
def enter_name():
    name = input("Enter student name:")
    return name

def enter_age():
    repeat=True
    while repeat:
        try:
            age = int(input("Enter student age:"))
            repeat=False
        except Exception:
            print("the age is wrong, try again ")
    return age
def enter_gender():
    repeat = True
    while repeat:
        try:
            gender = int(input("Enter student gender. Enter 1 if the student is Male, or "
                               "enter 2 if the student is female:"))
            if gender!=1 and gender!=2:
                raise Exception
            repeat = False
        except Exception:
            print("Invalid entered number! ")
    return gender

def enter_ssn(name):
    repeat=True
    while repeat:
        try:
            temp = "Enter " + name + "'s SSN:"
            ssn = int(input(temp))
            repeat=False
        except Exception:
            print("the ssn is wrong, try again ")
    return ssn

def enter_id():
    repeat=True
    while repeat:
        try:
            id=int(input("Enter student's ID:"))
            repeat=False
        except Exception:
            print("the id is wrong, try again ")
    return id

def enter_gpa():
    repeat=True
    while repeat:
        try:
            gpa=float(input("Enter student's GPA out of 5:"))

            if 0<=gpa<=5:
                repeat = False
            else:
                raise Exception

        except Exception:
            print("the gpa is wrong, try again ")
    return gpa


def enter_student():
    name=enter_name()
    age=enter_age()
    gender=enter_gender()
    ssn=enter_ssn(name)
    id=enter_id()
    gpa=enter_gpa()
    s=Student(name,age,gender,ssn,id,gpa)
    return s

def print_student(s):
    print("Student name:",s.get_name())
    print("Age:",s.get_age())
    if s.get_gender()==1:
        print("Gender: Male")
    else:
        print("Gender: Female")
    print("SSN: ",s.get_ssn())
    print("Student ID:",s.get_id())
    print("Student GPA:",s.get_gpa())


s=enter_student()
print_student(s)