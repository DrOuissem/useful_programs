
class Student:
    __slots__ = ['__name','__age','__id','__grade']
    def __init__(self,name,age,id,grade=60):
        self.__name=name
        self.__age=age
        self.__id=id
        self.__grade=grade
    def __str__(self):
        return self.__name +' : '+str(self.__id)
    def __repr__(self):
        res=""
        res+='name:'+self.__name+'\n'
        res+='age:'+str(self.__age)+'\n'
        res+='id:'+str(self.__id)+'\n'
        res+='grade:'+str(self.__grade)
        return res
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def print_name(self):
        print(self.__name)
    def set_grade(self,grade):
        self.__grade=grade
    def set_age(self,age):
        self.__age=age
    #to compare <
    def __lt__(self, other):
        return self.__grade<other.__grade
    #>
    def __gt__(self, other):
        return self.__grade > other.__grade
    #<=
    def __le__(self, other):
        return self.__grade<=other.__grade
    #>=
    def __ge__(self, other):
        return self.__grade >= other.__grade
    #==
    def __eq__(self, other):
        return self.__grade==other.__grade

    def print_info(self):
        print("name:",self.name)
        print("age:",self.age)
        print("id:",self.id)

s1=Student("mohamed",20,2233,80)
s2=Student("mona",22,3311,80)
s1.print_info()
s2.print_info()
print(s1.get_name())


if (s1==s2):
    print("students are equal")
else:
    print("students are different")

'''

student1=Student("Mohamed",20,2233)
student1.print_info()
print(student1)
print('hello')
print(repr(student1))
student2=Student("Mona",21,3344)
s=str(student2)
#print(student1,student2,sep='\n')
l=[student1,student2,Student("Khalid",23,1111),Student("Abeer",22,2222)]
for s in l:
    print(s)
#print(s)
#print(student1)
#print("all info about student1:")
#print(repr(student1))
#student1.print_info()
#print("=========")
#student2.print_info()


name_student1='Mohamed'
id_student1=2233
age_student1=20

name_student2='Mona'
age_student2=21
id_student2=3344

'''