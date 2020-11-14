
def name_function(param1=0,param2=0):
    print(param1,param2)

def my_function():
    print("hello")

#a(3,4)

'''
name_function(2,3)
name_function(2)
'''
def use_function(f):
    print("name of the function is :",f.__name__)
    f()

if __name__=='__main__':
    print("functions : ", __name__)
    a = name_function
    use_function(my_function)
    use_function(name_function)